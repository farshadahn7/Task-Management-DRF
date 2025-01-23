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

class ChangePasswordSerializers(serializers.Serializer):
    old_password = serializers.CharField(max_length=255, write_only=True)
    new_password = serializers.CharField(max_length=255, write_only=True)
    new_password1 = serializers.CharField(max_length=255, write_only=True)

    def validate(self, attrs):
        print(attrs)
        user_obj = self.context.get('request').user
        if attrs.get('new_password') != attrs.get('new_password1'):
            raise serializers.ValidationError("Password are not equal")

        if not user_obj.check_password(attrs.get("old_password")):
            raise serializers.ValidationError({'details': "Old Password is incorrect."})
        try:
            validate_password(attrs.get('new_password'))
        except ValidationError as e:
            raise serializers.ValidationError({"details": list(e.messages)})
        return super().validate(attrs)

    def update(self, instance, validated_data):
        del validated_data["old_password"]
        del validated_data["new_password1"]
        print(validated_data)
        instance.set_password(validated_data.get('new_password'))
        instance.save()
        return instance