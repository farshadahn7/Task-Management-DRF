from rest_framework.response import Response
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from ...models import Task
from .serializers import TaskSerializers


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'due_date']
    search_fields = ['title']
