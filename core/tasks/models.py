from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

CustomUser = get_user_model()

class Task(models.Model):
    class Status(models.TextChoices):
        Pending = ('P', 'pending')
        In_progress = ('I', 'in_progress')
        Completed = ('C', 'completed')

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.Pending)
    assigned_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.title

    def get_api_absolute_url(self):
        return reverse('task:api-v1:task-detail', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['created_date']
        indexes = [
            models.Index(fields=['created_date'])
        ]
