
from rest_framework import serializers
from .models import Restaurant,RestaurantStatistics

class RestaurantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Restaurant
        fields = '__all__'

class RestaurantStatisticsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RestaurantStatistics
        fields = ('count','avg','std' )
        