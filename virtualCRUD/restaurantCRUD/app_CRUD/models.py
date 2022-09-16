from random import choices
from django.db import models
from django.utils import timezone

class Restaurant(models.Model):
    
    class RatingIntegerChoices(models.IntegerChoices):
        
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
    
    id = models.CharField(verbose_name='Identifier', max_length=100,primary_key=True,unique=True)
    rating = models.IntegerField(choices=RatingIntegerChoices.choices,default='Zero')
    name =models.CharField(verbose_name='Name', max_length=100)
    site = models.CharField(verbose_name='URL', max_length=100)
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(verbose_name='Phone', max_length=100)
    street = models.CharField(verbose_name='Street', max_length=100)
    city = models.CharField(verbose_name='City', max_length=100)
    state = models.CharField(verbose_name='State', max_length=100)
    lat = models.FloatField(verbose_name='Latitude')
    lng = models.FloatField(verbose_name='Longitude')
    
    def __str__(self):
        return  self.name

class RestaurantStatistics(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField()
    avg = models.FloatField()
    std = models.FloatField()
    
    def __str__(self):
        return self.count


