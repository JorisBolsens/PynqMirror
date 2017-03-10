import time
import argparse

import feedparser
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# import matplotlib.pyplot as plt
# from pynq.pl import Overlay

from Mirror import Mirror

# Overlay("base.bit").download()

parser = argparse.ArgumentParser()
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

config = parser.parse_args()
mirror = Mirror()

mirror.email.connect(config.email_user, config.email_pass, config.imap_host)
mirror.email.get_mail()

image = Image.new('RGB', (1080,1920))
temp_font = ImageFont.truetype('Roboto-Medium.ttf', 45)

draw = ImageDraw.Draw(image)
wwid, wheight = temp_font.getsize(str(mirror.weather.temp)+'°')
draw.text((1080-50-(wwid),80), str(mirror.weather.temp)+'°', fill=(255,255,255), font=temp_font)

subject_font = ImageFont.truetype('RobotoCondensed-Regular.ttf', 25)
body_font = ImageFont.truetype('RobotoCondensed-Regular.ttf', 15)

emails = mirror.email.mails
prev_height = 0
max_subj = 0
for mail in emails:
    subject = mail['Subject'].strip()
    body = ''.join(e for e in mail['Body'] if e.isalnum() or e.isspace()).strip()

    t_subj = (subject[:48] + '..') if len(subject) > 50 else subject
    t_body = (body[:48] + '..') if len(body) > 50 else body

    t_body = t_body.replace('\r', '').replace('\n', ' ')

    subject_w, subject_h = subject_font.getsize(t_subj)
    body_w, body_h = body_font.getsize(t_body)

    if subject_w > max_subj:
        max_subj = subject_w

    draw.text((50, 80 + prev_height), t_subj, fill=(255,255,255), font=subject_font)
    prev_height += subject_h
    draw.text((50, 80 + prev_height), t_body, fill=(255, 255, 255), font=body_font)
    prev_height += body_h + 10

draw.rectangle(((40, 70), (60+max_subj, 90+prev_height)), outline=(255,255,255))

feed = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml?edition=us')
titles = []
for entry in feed.entries:
    titles.append(entry['title'])

# implt = plt.imshow(image.rotate(90, expand=True))
# plt.show()

news_font = ImageFont.truetype('RobotoCondensed-Regular.ttf', 10)
for title in titles:


mirror.display.show_frame(image.rotate(90, expand=True).tobytes())

time.sleep(20)