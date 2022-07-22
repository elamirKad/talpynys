from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    reward = models.FloatField()
    completed = models.BooleanField(default=False)
