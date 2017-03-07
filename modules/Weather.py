import requests

# from pynq.iop import PMODA
# from pynq.iop import Pmod_TMP2


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
        self.temp = 48.98
        # weather=requests.get('http://api.openweathermap.org/data/2.5/weather?lat='
        #                       +str(self.lat)
        #                       +'&lon='
        #                       +str(self.long)
        #                       +'&units=imperial'
        #                       +'&appid='
        #                       +self.app_id)
        # self.temp = weather.json()['main']['temp']
        # self.icons = [requests.get('https://openweathermap.org/img/w/'+weather_dat['icon']+'.png') for weather_dat in
        #                            weather.json()['weather']]
        # mytmp = Pmod_TMP2(PMODA)
        # temperature = mytmp.read()
        # self.temp=9.0/5.0 * temperature + 32

    def update_weather(self):
       self._get_weather()