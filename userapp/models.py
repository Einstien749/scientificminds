from django.db import models

from django.shortcuts import reverse

from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    picture = models.ImageField(upload_to="userimage", default="userimage/user.png")

    def __str__(self):

        return str(self.email)

    def get_absolute_url(self):

        return reverse("login")
