
import requests as req
from geopy import distance
from django.http import HttpResponseRedirect,HttpResponse
import statistics 
from .models import RestaurantStatistics



def get_dataJson_APIrestaurants():
    url='http://127.0.0.1:8000/api/restaurants/?format=json'
    res = req.get(url)
    post = res.json()
    return post

#input_urse=(17.048461376336846,-96.69138479711978 )
def get_restaurants_radio(ubi_rest,dist):
    dist=float(dist)
    
    new_api = []
    for name in get_dataJson_APIrestaurants():
        lat = name.get('lat')
        long = name.get('lng')
        data = lat,long
        new_distance= distance.distance(ubi_rest,data).meters
        if new_distance <= dist:
            new_api.append(name)
            
                
                
    return new_api

#print(get_restaurants_radio(input_urse))
#rating: 4,2,4
def get_avg_std_count(request,params):
    params=params.split('&')
    data=[]
    for item in params:
        data.append(item.split('=')[1])
    lat=data[0]
    lng=data[1]
    dist=data[2]
    ubi=float(lat),float(lng)
    
    new_json = get_restaurants_radio(ubi,dist)
    list_rating=[]    
    
    for data in new_json:
        list_rating.append(data.get('rating'))
    
    try:
        get_count = len(list_rating)
        get_avg= sum(list_rating)/get_count
        get_std = statistics.pstdev(list_rating)
    except:
        return HttpResponse("Upss!! Al parecer no hay registros con esos parametros. Intenta incrementar el radio")
    try:
        data_BD_ResSta = RestaurantStatistics.objects.all()
        data_BD_ResSta.delete()
    except :
        print('Error al limpiar BD')
        
    save_data_Rest = RestaurantStatistics(count=get_count, avg=get_avg, std=get_std )
    save_data_Rest.save(force_insert=True)
    
    
    
    return HttpResponseRedirect('http://127.0.0.1:8000/api/statistics/')
    
    
#params='restaurants/statistics/latitude=17.048461376336846&longitude=-96.69138479711978&radius=1'
