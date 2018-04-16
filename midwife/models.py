from django.db import models

# Create your models here.
class Location(models.Model):
    county = models.CharField(max_length=50)

    @classmethod
    def inputed_county(cls):
        '''
        Method that gets list of users location
        '''
        loc = cls.objects.all()
        return loc

class Town(models.Model):
    nearest_town = models.CharField(max_length=50)

    @classmethod
    def inputed_town(cls):
        '''
        Method that gets list of users location
        '''
        area = cls.objects.all()
        return area

class User(models.Model):
    name = models.CharField(max_length=60, null=True)
    type_of_user = models.CharField(max_length=30, null=True)
    national_id= models.IntegerField(null=True)
    phonenumber= models.CharField(max_length=60)
    county = models.ManyToManyField(Location)
    nearest_town = models.ManyToManyField(Town)
    level = models.IntegerField(null=True)

    @classmethod
    def requested_users(cls, user_type):
        '''
        Method that gets list of farmers for buyer and vice versa
        '''
        if user_type == '1':
            requested_type = '2'
        else:
            requested_type = '1'

        found_users = User.objects.filter(type_of_user=requested_type)
        return found_users

class session_levels(models.Model):
	session_id = models.CharField(max_length=25,primary_key=True)
	phonenumber= models.CharField(max_length=25,null=True)
	level = models.IntegerField(null=True)
