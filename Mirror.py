# from modules.Display import Display
from modules.Email import Email
from modules.Weather import Weather

class Mirror(object):

    def __init__(self):
        self.weather = Weather()
        # self.display = Display()
        self.email = Email()