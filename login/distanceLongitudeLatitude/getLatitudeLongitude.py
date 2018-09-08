from django.conf import settings
import requests

def getLatitudeLongitude(address):
    address = address
    api_key = getattr(settings, "API_KEY", None)
    #api_key = "AIzaSyByHNzULe2W4eE2LAVH1NiA-NtInV-5EoQ"
    api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
    api_response_dict = api_response.json()
    if api_response_dict['status'] == 'OK':
        latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        longitude = api_response_dict['results'][0]['geometry']['location']['lng']
        #print latitude, longitude
        return latitude, longitude
    else:
        return "0", "0"
        
getLatitudeLongitude("Av. Paseo de Los Heroes 10999, Zona Ro, 22010 Tijuana, B.C., Mexico")