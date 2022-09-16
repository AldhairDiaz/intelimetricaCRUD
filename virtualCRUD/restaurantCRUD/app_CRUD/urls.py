from django.urls import path
from rest_framework import routers
from .viewsets import RestaurantViewSet,RestaurantStatisticsViewSet


route = routers.SimpleRouter()
route.register('restaurants',RestaurantViewSet)
route.register('statistics',RestaurantStatisticsViewSet)


urlpatterns = route.urls