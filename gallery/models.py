from django.db import models
from django.forms import ImageField


class Image(models.Model):
    name = models.CharField(max_length = 60)
    photo = models.ImageField(upload_to = 'uploads/')
    description = models.TextField()
    
# Create your models here.
