from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60, null=True)
    type_of_user = models.CharField(max_length=30, null=True)
    national_id= models.IntegerField(null=True)
    phonenumber= models.CharField(max_length=60)
    location = models.CharField(max_length=60, null=True)
    nearest_town = models.CharField(max_length=50)