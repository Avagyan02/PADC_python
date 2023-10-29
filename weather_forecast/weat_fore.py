import requests
from credentials import api_key

class WeatherApi:
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def __init__(self):
        while True:
            city = input('Write the city: ')
            self.city = city
            url = self.base_url + "appid=" + api_key + "&q=" + city
            self.get_weather_info(url)

    def get_weather_info(self, url):
        response = requests.get(url).json()

        if ('message' in response and response['message'] == 'city not found') or self.city.isdigit():
            print('Print valid city name')
            return

        temp_kelvin = response['main']['temp']
        celcius = temp_kelvin - 273
        fahrenheit = celcius * (9 / 5) + 32
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celcius = feels_like_kelvin - 273
        feels_like_fahrenheit = feels_like_celcius * (9 / 5) + 32
        wind_speed = response['wind']['speed']
        humidity = response['main']['humidity']
        city = self.city[0].upper() + self.city[1::]

        print(f"Temperature in {city} is {celcius}°C or {fahrenheit}°F")
        print(f"Temperature in {city} feels like {feels_like_celcius}°C or {feels_like_fahrenheit}°F")
        print(f"Humidity in {city} is {humidity}%")
        print(f"Wimd Speed in {city} is {wind_speed}m/s")