from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from mail_templated import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from decouple import config
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from rest_framework.permissions import IsAuthenticated

from .serializers import RegistrationSerializers, CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer, ChangePasswordSerializers
from ...models import CustomUser


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializers

    @staticmethod
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def post(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        user_obj = get_object_or_404(CustomUser, username=serialized_data.data['username'])
        user_token = self.get_tokens_for_user(user_obj)
        send_mail('email/verification_email.tpl', {'user': user_obj.username, 'token': user_token}, 'admin@admin.com',
                  [user_obj.email])
        return Response("You are registered successfully.Please check your email for verification.")

class AccountVerificationView(APIView):
    def get(self, request, token, *args, **kwargs):
        try:
            user_data = jwt.decode(token, config('SECRET_KEY'), algorithms=["HS256"])
            user_obj = get_object_or_404(CustomUser, id=user_data['user_id'])
            user_obj.is_verified = True
            user_obj.save()
        except ExpiredSignatureError:
            return Response("Link is Expired")
        except InvalidTokenError:
            return Response("link is invalid.")
        return Response({'details': "Your account is verified successfully."})

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer

class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializers
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        return self.request.user