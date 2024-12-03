from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from .serializers import ChangePasswordSerializer, SignInSerializer,
from rest_framework.exceptions import ValidationError

# Create your views here.



class SigninPasswordView(APIView):
    serializer_class = SignInSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=200)
        except ValidationError as exc:
            error_codes = exc.get_codes() or 400
            code = next(iter(error_codes.values()))[0] if error_codes else 400
            print(code)
            return Response(
                exc.detail, 
                status=code
            )


class ChangePaswordView(APIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [OAuth2Authentication, JWTAuthentication]

    def put(self, request):
        context = {
            'request':request
        }
        serializer = self.serializer_class(data=request.data, context=context)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({'message': 'password change successfully'}, status=status.HTTP_200_OK)
        except ValidationError as exc:
            error_codes = exc.get_codes() or 400
            code = next(iter(error_codes.values()))[0] if error_codes else 400
            print(code)
            return Response(
                exc.detail, 
                status=code  
            )