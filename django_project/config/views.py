from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView
from rest_framework.permissions import IsAdminUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
       

        return token
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomSpectacularSwaggerView(SpectacularSwaggerView):
    permission_classes = [IsAdminUser] 


class CustomSpectacularRedocView(SpectacularRedocView):
    permission_classes = [IsAdminUser]  