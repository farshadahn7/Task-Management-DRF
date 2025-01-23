from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'assigned_user', 'status', 'created_date', 'updated_date', 'due_date']
    list_filter = ['title', 'assigned_user']
