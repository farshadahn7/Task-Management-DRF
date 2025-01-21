from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



from .serializers import RegistrationSerializers, CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer

class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializers
    def post(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response("You registered successfully.")


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer