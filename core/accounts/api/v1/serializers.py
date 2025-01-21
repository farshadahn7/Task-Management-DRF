from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from ...models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

class RegistrationSerializers(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'password1']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError("passwords dont match.")

        try:
            validate_password(attrs.get('password'))
        except ValidationError as e:
            raise serializers.ValidationError({'details':list(e.messages)})

        attrs.pop('password1')
        return super().validate(attrs)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        if '@' in attrs.get('username'):
            if CustomUser.objects.filter(email=attrs.get('username')).exists():
                user_name = CustomUser.objects.filter(email=attrs.get('username')).first().username
                attrs.pop('username')
                attrs['username'] = user_name
        data = super().validate(attrs)
        data['user'] = self.user.username
        data['email'] = self.user.email
        data['user_id'] = self.user.id
        return data

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    pass

