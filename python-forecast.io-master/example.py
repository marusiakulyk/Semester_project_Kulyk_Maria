import datetime
import forecastio
from geopy.geocoders import Nominatim

def main(city):
    """
    Run load_forecast() with the given lat, lng, and time arguments.
    """

    api_key = "7a9f9b37ebe0fddb2aec86405a972ff6"
    geolocator = Nominatim()
    location1 = geolocator.geocode(city)
    lat = location1.latitude
    lng = location1.longitude
    time = datetime.datetime.now()

    forecast = forecastio.load_forecast(api_key, lat, lng, time=time)

    print("===========Currently Data=========")
    print(forecast.currently())

    print("===========Hourly Data=========")
    by_hour = forecast.hourly()
    print("Hourly Summary: %s" % by_hour.summary)

    for hourly_data_point in by_hour.data:
        print(hourly_data_point)

    print("===========Daily Data=========")
    by_day = forecast.daily()
    print("Daily Summary: %s" % by_day.summary)

    for daily_data_point in by_day.data:
        print(daily_data_point)

if __name__ == "__main__":
    main('Lviv')
