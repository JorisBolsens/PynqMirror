import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from Mirror import Mirror
from Display import Display


mirror = Mirror()
display = Display()
temp = mirror.weather.temp

image = Image.new('RGB', (1080,1920))
font = ImageFont.truetype('Roboto-Medium.ttf', 65)

draw = ImageDraw.Draw(image)
wwid, wheight = font.getsize(str(temp)+'°')
draw.text((1080-160-(wwid),130), str(temp)+'°', fill=(255,255,255), font=font)
display.show_frame(image.tobytes())