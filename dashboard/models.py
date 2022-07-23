from django.db import models

# Create your models here.
class ProfilePic(models.Model):
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
