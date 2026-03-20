import requests
from geopy.geocoders import Nominatim

def apifetch():
    url = ("https://api.wheretheiss.at/v1/satellites/25544")
    response = requests.get(url,timeout=15)
    if response.status_code == 200:
        print("API IS ONLINE")
    else:
        print("API SEEMS TO BE CAUSING ERORS", response.status_code)
    data = response.json()
    time = data["timestamp"]
    lat =  float(data["latitude"])
    long = float(data["longitude"])
    position = (lat,long)
    return position,time 


(position, time) = apifetch()
lat, long = position
coordinates = lat, long



def reversen_nominatim():
    geolocator = Nominatim(user_agent="iss_tracker_by_wafi")
    georeverse = geolocator.reverse(f"{lat},{long}")
    if georeverse is not None:
        location = georeverse.address
        return location
    return "Over the Ocean"
    

