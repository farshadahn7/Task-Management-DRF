from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


class CustomManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("Username must be set")
        if not email:
            raise ValueError("Email must be set.")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Super user must be True")
        if extra_fields.get('is_active') is not True:
            raise ValueError("Active must be True")
        if extra_fields.get('is_staff') is not True:
            raise ValueError("staff must be True")
        if extra_fields.get('is_verified') is not True:
            raise ValueError("verified must be True")

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    firs_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = CustomManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.firs_name} {self.last_name}"
