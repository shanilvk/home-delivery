from django.db import models

# Create your models here.

class foods(models.Model):
    item=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='food_images')