from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    contact_no = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
