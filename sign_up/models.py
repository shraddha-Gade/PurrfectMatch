from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    contact_no = models.CharField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
