from django.test import TestCase
from django.contrib.auth import get_user_model


from ..models import Task

CustomUser = get_user_model()


class TestTaskModel(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username="test", email="test@test.com", password="123456@a"
        )
        self.task = Task.objects.create(
            title="test",
            description="This is desc",
            status="p",
            assigned_user=self.user,
        )

    def test_create_task(self):
        self.assertTrue(Task.objects.filter(id=self.task.id).exists())
