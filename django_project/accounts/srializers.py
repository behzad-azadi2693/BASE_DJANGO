from django.contrib.auth import authenticate
from oauth2_provider.models import AccessToken, RefreshToken, get_application_model
import datetime, random, secrets
from decouple import config


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)
    token_type = serializers.CharField(read_only=True)
    expires_in = serializers.CharField(read_only=True)


    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        client_id = config('CLIENT_ID')
        if not user:
            raise serializers.ValidationError({"error": "Invalid credentials"}, status=401)

        # Validate client
        Application = get_application_model()
        try:
            application = Application.objects.get(client_id=client_id)
        except Application.DoesNotExist:
            raise serializers.ValidationError({"error": "Invalid client"}, status=400)
        
        return attrs

    def create(self, validated_data):
        user = authenticate(username=validated_data['username'], password=validated_data['password'])
        application = get_application_model().objects.get(client_id=config('CLIENT_ID'))
        # Generate tokens
        expires = datetime.datetime.now() + datetime.timedelta(hours=1)
        input_string = f"{user.username}-{secrets.token_urlsafe(32)}-{user.id}"
        access_token = AccessToken.objects.create(
            user=user,
            application=application,
            token=''.join(random.sample(input_string, len(input_string))),  # Generate unique token
            expires=expires,
            scope="read write"
        )
        refresh_token = RefreshToken.objects.create(
            user=user,
            token=secrets.token_urlsafe(64),  # Generate unique token
            access_token=access_token,
            application=application
        )

        return {
            "access_token": access_token.token,
            "refresh_token": refresh_token.token,
            "token_type": "Bearer",
            "expires_in": (expires - datetime.datetime.now()).seconds,
        }


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    password_confierm = serializers.CharField(required=True)

    def validate(self, attrs):
        user = User.objects.filter(id=self.context['request'].user.id, is_active=True).first()
        if not user:
            raise serializers.ValidationError({"user":"user is not exsits"}, code=401)
        if attrs['password'] != attrs['password_confierm']:
            raise serializers.ValidationError({"password":"Passwords is not match."}, code=400)
        return attrs
        
    def create(self, validated_data):
        user = User.objects.get(id=self.context['request'].user.id)
        # Update password for the existing user
        user.set_password(validated_data['password'])
        user.save()

        return user