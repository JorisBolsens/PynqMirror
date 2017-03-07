# import time
import argparse

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# from pynq.pl import Overlay

from Mirror import Mirror

# Overlay("base.bit").download()

parser = argparse.ArgumentParser()
parser.add_argument()
parser.add_argument("--imap-host",
                    "-ih",
                    help="Email host to pass to Email client (Optional)",
                    type=str,
                    default="imap.gmail.com",
                    dest="imap_host")
parser.add_argument("--email-user",
                    "-eu",
                    help="Email username to pass to Email client (Required)",
                    type=str,
                    dest="email_user")
parser.add_argument("--email-pass",
                    "-ep",
                    help="Email password to pass to Email client (Required)",
                    type=str,
                    dest="email_pass")
mirror = Mirror()
temp = mirror.weather.temp

image = Image.new('RGB', (1080,1920))
font = ImageFont.truetype('Roboto-Medium.ttf', 65)

mirror.email.get_maill()

draw = ImageDraw.Draw(image)
wwid, wheight = font.getsize(str(temp)+'°')
draw.text((1080-50-(wwid),80), str(temp)+'°', fill=(255,255,255), font=font)

# mirror.display.show_frame(image.rotate(90, expand=True).tobytes())
