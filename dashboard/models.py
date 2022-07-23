from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfilePic(models.Model):
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

class AccountExperience(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.FloatField()