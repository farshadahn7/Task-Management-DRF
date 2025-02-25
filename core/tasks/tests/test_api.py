import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime


from ..models import Task

CustomUser = get_user_model()


@pytest.fixture
def test_user():
    return CustomUser.objects.create(
        username="test", email="test@test.com", password="123456@a"
    )


@pytest.fixture
def test_superuser():
    return CustomUser.objects.create(
        username="test", email="test@test.com", password="123456@a", is_staff=True
    )


@pytest.fixture
def test_task(test_user):
    user_obj = test_user
    data = {
        "title": "test",
        "description": "test des",
        "status": "P",
        "assigned_user": user_obj,
        "due_date": datetime.now(),
    }
    task = Task.objects.create(**data)
    return task


@pytest.mark.django_db(True)
class TestTaskApi:
    client = APIClient()

    def test_retrieve_tasks_response(self):
        url = reverse("task:api-v1:task-list")
        res = self.client.get(url)
        assert res.status_code == 200

    def test_create_task_normal_user_response(self, test_user):
        # Normal user Cant create a task
        self.client.force_authenticate(test_user)
        url = reverse("task:api-v1:task-list")
        data = {
            "title": "test",
            "description": "test des",
            "status": "P",
            "assigned_user": test_user.id,
            "due_date": datetime.now(),
        }
        res = self.client.post(url, data)
        assert res.status_code == 403

        user_obj = test_user
        user_obj.is_staff = True
        self.client.force_authenticate(user_obj)
        res = self.client.post(url, data)
        assert res.status_code == 201

    def test_partial_update_task_normal_user_response(self, test_task, test_user):
        # Normal user Cant partially update the task (In this url)
        task = test_task
        self.client.force_authenticate(test_user)
        url = reverse("task:api-v1:task-detail", kwargs={"slug": task.slug})
        res = self.client.patch(url, data={"description": "changed"})
        assert res.status_code == 403

        # superuser which is_staff field is True can partially update the task
        user_obj = test_user
        user_obj.is_staff = True
        self.client.force_authenticate(user_obj)
        res = self.client.patch(url, data={"description": "changed"})
        assert res.status_code == 200

    def test_update_task_response(self, test_task, test_user):
        # Normal user Cant update the task
        task = test_task
        user_obj = test_user
        self.client.force_authenticate(user_obj)
        url = reverse("task:api-v1:task-detail", kwargs={"slug": task.slug})
        new_data = {
            "title": "test changed",
            "description": "test des changed",
            "status": "P",
            "assigned_user": user_obj.id,
            "due_date": datetime.now(),
        }
        res = self.client.patch(url, data=new_data, format="json")
        assert res.status_code == 403

        # superuser which is_staff field is True can update the task
        user_obj.is_staff = True
        self.client.force_authenticate(user_obj)
        res = self.client.patch(url, data=new_data, format="json")
        assert res.status_code == 200

    def test_delete_task_response(self, test_task, test_user):
        # Normal user Cant delete the task
        task = test_task
        self.client.force_authenticate(test_user)
        url = reverse("task:api-v1:task-detail", kwargs={"slug": task.slug})
        res = self.client.delete(url)
        assert res.status_code == 403

        # superuser which is_staff field is True can delete the task
        test_user.is_staff = True
        self.client.force_authenticate(test_user)
        res = self.client.delete(url)
        assert res.status_code == 204


@pytest.mark.django_db(True)
class TestUserTaskApi:
    client = APIClient()

    def test_retrieve_users_task_response(self, test_user, test_task):
        self.client.force_authenticate(test_user)
        url = reverse("task:api-v1:user-task", kwargs={"slug": test_task.slug})
        res = self.client.get(url)
        assert res.status_code == 200

    def test_partially_update_users_task_response(self, test_task, test_user):
        self.client.force_authenticate(test_user)
        url = reverse("task:api-v1:user-task", kwargs={"slug": test_task.slug})
        res = self.client.patch(url, data={"status": "I"})
        assert res.status_code == 200
