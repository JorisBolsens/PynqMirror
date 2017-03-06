import requests
import json

class Weather(object):

    def __init__(self):
        self.app_id = '9115ff1468e12338e0b7121be110dafb'
        self._get_loc()
        self._get_weather()

    def _get_loc(self):
        loc_url = 'https://freegeoip.net/json'
        resp = requests.send(loc_url)
        js = json.loads(resp)
        self.long = js['longitude']
        self.lat = js['latitude']

    def _get_weather(self):
        weather=requests.send('https://api.openweathermap.org/data/2.5/weather?lat='
                              +self.lat
                              +'&lon='
                              +self.long
                              +'&appid='
                              +self.app_id)
        weather_json = json.loads(weather)
        self.temp = weather_json['main']['temp']
        self.icons = [weather_dat['icon'] for weather_dat in weather_json['weather']]

    def update_weather(self):
       self._get_weather()