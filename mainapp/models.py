from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    reward = models.FloatField()
    username = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

class Comment(models.Model):
    task_id = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    comment = models.TextField()

class Executor(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
