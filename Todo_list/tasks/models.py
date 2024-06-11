from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
]

# Create your models here.
class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=240)
    due_date = models.DateField()
    notes = models.TextField(blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    completion_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')


    def get_dynamic_url(self):
        return reverse("Dynamic", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("deleteview", kwargs={"id": self.id})
 
    def get_edit_url(self):
        return reverse("editview", kwargs={"id": self.id})