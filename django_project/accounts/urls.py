from django.urls import path
from .views import  SigninPasswordView

app_name = 'accounts'

urlpatterns = [
    path('password/signin/', SigninPasswordView.as_view(), name='register'),
]