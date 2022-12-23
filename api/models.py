from django.db import models
from datetime import datetime

# Create your models here.
class Cast(models.Model):
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    dob=models.DateField()

    def __str__(self):
        return self.name 
      
class Movie(models.Model):
     title=models.CharField(max_length=100)
     cast=models.ForeignKey(Cast,on_delete=models.CASCADE,related_name='sungby')
     created_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now=True)
     runtime=models.IntegerField()
     language=models.CharField(max_length=100)
     tagline =models.CharField(max_length=200)

     def __str__(self):
        return self.title 
        