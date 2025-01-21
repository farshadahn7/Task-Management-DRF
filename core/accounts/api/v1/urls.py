from django.urls import path

from . import views

app_name = 'api-v1'

urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='registration'),
]
