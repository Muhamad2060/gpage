from django.db import models

# Create your models here.

class Students(models.Model):
    # id = models.AutoField()  this is automaticile put by django to count our data 

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
   

class Cars(models.Model):
    car_name = models.CharField(max_length=100)
    car_speed = models.IntegerField(default=50)
    
    def __str__(self):
        return self.car_name

