from rest_framework.response import Response
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


from ...models import Task
from .serializers import TaskSerializers


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'due_date']