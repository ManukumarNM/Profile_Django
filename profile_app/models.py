from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200, blank=True, null=True)
	last_name = models.CharField(max_length=200, blank=True, null=True)
	email = models.CharField(max_length=200)
	profile_pic = models.ImageField(null=True, blank=True, upload_to="profile_pics", default="profile_pics/default.png")
	bio = models.TextField(null=True, blank=True)
	linked_in = models.CharField(max_length=200,null=True, blank=True)

	def __str__(self):
		name = str(self.first_name)
		if self.last_name:
			name += ' ' + str(self.last_name)
		return name

class Contact(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.name 