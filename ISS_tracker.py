import requests

def apifetch():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    if response.status_code == 200:
        print("API IS ONLINE")
    else:
        print("API SEEMS TO BE CAUSING ERORS", response.status_code)
    data = response.json()
    time = data["timestamp"]
    lat = float(data["iss_position"]["latitude"] )
    long = float(data["iss_position"]["longitude"])
    position = (lat,long)
    return position,time 


(position, time) = apifetch()
lat, long = position
print(lat,long,time)
