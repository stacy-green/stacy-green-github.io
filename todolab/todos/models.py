from django.db import models
from django.contrib.auth.models import User


class Priority(models.Model):
    name = models.CharField(max_length=10)
    priority = models.IntegerField()

    def __str__(self):
        return f"({self.priority}) {self.name}"


class TodoItem(models.Model):
    text = models.CharField(max_length=240)
    priority = models.ForeignKey(
        Priority, on_delete=models.PROTECT, related_name="todos")

    completed_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="todos")

    def __str__(self):
        return self.text[:20]
