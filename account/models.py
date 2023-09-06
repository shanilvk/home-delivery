from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    message=models.TextField()
    added_on=models.DateField(auto_now_add=True)
    is_approved=models.BooleanField(default=True)
    
    
    def __str__(self): 
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Table"
        
        
        
# class Vegetarian(models.Model):
#     item= models.CharField(max_length=250)
#     price=models.IntegerField()
#     image=models.ImageField()

    
# class Nonveg(models.Model):
#     item= models.CharField(max_length=250)
#     price=models.IntegerField()
#     image=models.ImageField()
    
    
# class Beverages(models.Model):
#     item= models.CharField(max_length=250)
#     price=models.IntegerField()
#     image=models.ImageField()
    

     