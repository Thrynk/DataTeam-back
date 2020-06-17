# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db.models import Q


def recup_meteo(latitude, longitude, city=None):
    from api.models import Meteo , City
    from datetime import datetime 
    from geopy.geocoders import Nominatim

    # Import Meteo model from Django
    import os
    
    # Import requests and Basic auth
    import requests
    from requests.auth import HTTPBasicAuth
    
    # request data from API
    url_base = 'https://api.meteomatics.com/'
    
    date = datetime.now()
    #print(timezone.now())
    dateString = date.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    number_of_days = 7
    number_of_values_per_hour = 1
    
    temperature_parameter = 't_0m:C'
    humidity_parameter = 'relative_humidity_2m:p'
    precipitation_parameter = 'precip_1h:mm'
    
    url = url_base \
        + dateString \
        + 'P' + str(number_of_days) + 'D:PT' + str(number_of_values_per_hour) + 'H/' \
        + temperature_parameter + ',' + humidity_parameter + ',' + precipitation_parameter + '/' \
        + str(latitude) + ',' + str(longitude) \
        + '/json?model=mix'

    #print(url)
    
    r = requests.get(url, auth=HTTPBasicAuth('isen_meunier', 'rT2ql81CVUzpS'))

    #a='https://api.meteomatics.com/2020-06-15T17:18:30ZP7D:PT1H/t_0m:C,relative_humidity_2m:p,precip_1h:mm/50.6,3.06/json?model=mix'
   
    data = r.json()
    
    # temperature
    #print(len(data["data"][0]["coordinates"][0]["dates"]))
    ## humidity
    #print(len(data["data"][1]["coordinates"][0]["dates"]))
    ## precipitation
    #print(len(data["data"][2]["coordinates"][0]["dates"]))
    
    Meteo.objects.filter(location_latitude=latitude, location_longitude=longitude).delete()
    if city is None:
        geolocator = Nominatim("my_application")
        location = geolocator.reverse("{latitude}, {longitude}".format(latitude=latitude, longitude=longitude), exactly_one=True) 
        #location.address.split(",")[0]
        city=City.objects.create(location_longitude=longitude, location_latitude=latitude)#, name=location.address.split(",")[4])
    else:
        city=City.objects.get(id=city.id)
        city.last_load=datetime.now()
        city.save()
        Meteo.objects.filter(city=city).delete()

    for i in range(0, len(data["data"][0]["coordinates"][0]["dates"])):
        #print((data["data"][0]["coordinates"][0]["dates"][i]["date"])+"+00:00")
        dict={
            "city":city,
            "location_latitude":latitude,
            "location_longitude":longitude,
            "temperature":data["data"][0]["coordinates"][0]["dates"][i]["value"],
            "humidity":data["data"][1]["coordinates"][0]["dates"][i]["value"],
            "precipitation":data["data"][2]["coordinates"][0]["dates"][i]["value"],
            "date_time":data["data"][0]["coordinates"][0]["dates"][i]["date"],
            }
        queryset = Meteo(**dict)
        queryset.save()

    return city


#def meteo(latitude,longitude):
#    queryset = Meteo.objects.filter(
#        Q(latitude__gte=latitude)
#        )
        
if __name__ == "__main__":
    latitude = 50.6
    longitude = 3.06
    recup_meteo(latitude, longitude)