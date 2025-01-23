from rest_framework.response import Response
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView

from ...models import Task
from .serializers import TaskSerializers, UserTaskSerializers


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = Task.objects.all()
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'due_date']
    search_fields = ['title']


class UserTaskView(RetrieveUpdateAPIView):
    lookup_field = 'slug'
    serializer_class = UserTaskSerializers
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        request = self.request
        return Task.objects.filter(assigned_user=request.user.id)
