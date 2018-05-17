import datetime
import forecastio
from forecast_class import Forecast
from geopy.geocoders import Nominatim
from apixu.client import ApixuClient, ApixuException


api_key = "7a9f9b37ebe0fddb2aec86405a972ff6"
geolocator = Nominatim()
location1 = geolocator.geocode("Lviv")
lat = location1.latitude
lng = location1.longitude
time = datetime.datetime.now()
forecast1 = forecastio.load_forecast(api_key, lat, lng, time=time).json

api_key1 = "79c89a7b53c24ffb8de111947180304"
client = ApixuClient(api_key1)
forecast2 = client.getForecastWeather(q='Lviv', days=1)
print(str(forecast1))
print(str(forecast2))

a = Forecast()
forecastio = ['daily', 'data', 0]
apixu = ['forecast', 'forecastday', 0, 'day']
a.add(forecast1, forecastio + ['temperatureMin'], "min_temp")
a.add(forecast1, forecastio + ['temperatureMax'], "max_temp")
a.add(forecast2, apixu + ['maxtemp_c'], 'max_temp')
a.add(forecast2, apixu + ['mintemp_c'], 'min_temp')
print(a)
a.close()
print(a)

