from django.db import models

# Create your models here.
class Pet(models.Model):

    name = models.CharField(max_length = 100)
    species = models.CharField(max_length = 20)
    gender = models.CharField(max_length = 10)
    breed = models.CharField(max_length = 100 , blank = True , null = True)
    age = models.IntegerField()
    vaccinated = models.BooleanField()
    city = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'pet_images/')
    
