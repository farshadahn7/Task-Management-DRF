from django.urls import path, include

app_name = "task"

urlpatterns = [
    path("api/v1/", include("tasks.api.v1.urls")),
]
