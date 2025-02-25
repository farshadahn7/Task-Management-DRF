from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "api-v1"

rout = DefaultRouter()
rout.register("tasks", views.TaskViewSet, basename="task")

urlpatterns = [
    path("user/<slug:slug>/", views.UserTaskView.as_view(), name="user-task"),
]

urlpatterns += rout.urls
