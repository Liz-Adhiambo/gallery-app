from django.db import models
from django.forms import ImageField


class Image(models.Model):
    name = models.CharField(max_length = 60)
    photo = models.ImageField(upload_to = 'uploads/')
    description = models.TextField()
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



# Create your models here.
