from django.urls import path

from . import views

app_name = "api-v1"

urlpatterns = [
    path("registration/", views.RegistrationView.as_view(), name="registration"),
    path("login/", views.CustomTokenObtainPairView.as_view(), name="jwt_login"),
    path(
        "login_refresh/",
        views.CustomTokenRefreshView.as_view(),
        name="jwt_login_refresh",
    ),
    path(
        "verification/<str:token>/",
        views.AccountVerificationView.as_view(),
        name="verification",
    ),
    path(
        "change_password/", views.ChangePasswordView.as_view(), name="change_password"
    ),
]
