from rest_framework import viewsets
from .models import Restaurant,RestaurantStatistics
from .serielizer import RestaurantSerializer,RestaurantStatisticsSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantStatisticsViewSet(viewsets.ModelViewSet):
    
    queryset = RestaurantStatistics.objects.all()
    serializer_class = RestaurantStatisticsSerializer
