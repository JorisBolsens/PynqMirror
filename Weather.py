import requests

class Weather(object):

    def __init__(self):
        self.app_id = '9115ff1468e12338e0b7121be110dafb'
        self._get_loc()
        self._get_weather()

    def _get_loc(self):
        loc_url = 'https://freegeoip.net/json'
        resp = requests.get(loc_url)
        self.long = resp.json()['longitude']
        self.lat = resp.json()['latitude']

    def _get_weather(self):
        # weather=requests.get('http://api.openweathermap.org/data/2.5/weather?lat='
        #                       +str(self.lat)
        #                       +'&lon='
        #                       +str(self.long)
        #                       +'&units=imperial'
        #                       +'&appid='
        #                       +self.app_id)
        # self.temp = weather.json()['main']['temp']
        # self.icons = [weather_dat['icon'] for weather_dat in weather.json()['weather']]
        self.temp=48.98

    def update_weather(self):
       self._get_weather()