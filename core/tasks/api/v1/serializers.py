from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from ...models import Task


CustomUser = get_user_model()


class TaskSerializers(serializers.ModelSerializer):
    task_detail = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "title",
            "slug",
            "description",
            "status",
            "assigned_user",
            "due_date",
            "task_detail",
        ]
        read_only_fields = ["slug"]

    def get_task_detail(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(str(obj).lower().replace(" ", "-"))

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        user_obj = get_object_or_404(CustomUser, id=rep["assigned_user"])
        rep["assigned_user"] = user_obj.username
        if request.parser_context.get("kwargs").get("slug") is not None:
            rep.pop("slug")
            rep.pop("task_detail")
        else:
            rep.pop("description")
        return rep

    def create(self, validated_data):
        return super().create(validated_data)


class UserTaskSerializers(serializers.ModelSerializer):
    title = serializers.CharField(max_length=125, read_only=True)

    class Meta:
        model = Task
        fields = ["title", "description", "status", "assigned_user", "due_date"]
        read_only_fields = ["title", "description", "assigned_user", "due_date"]
