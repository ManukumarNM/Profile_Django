from django.db import models
from PIL import Image

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to="profile_pics")

    def __str__(self):
        return self.name 

class Contact(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.name 