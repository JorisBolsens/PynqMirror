import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pynq.pl import Overlay

from Mirror import Mirror
from Display import Display

Overlay("base.bit").download()


mirror = Mirror()
display = Display()
temp = mirror.weather.temp

image = Image.new('RGB', (1080,1920))
font = ImageFont.truetype('Roboto-Medium.ttf', 65)

draw = ImageDraw.Draw(image)
wwid, wheight = font.getsize(str(temp)+'°')
draw.text((1080-50-(wwid),80), str(temp)+'°', fill=(255,255,255), font=font)

display.show_frame(image.rotate(90, expand=True).tobytes())
