#!/usr/bin/env python3
import random
import urllib.request


def download_web_image(url):
    name = random.randrange(1, 10000)
    fullname = str(name) + ".jpeg"

    urllib.request.urlretrieve(url, filename=fullname)

download_web_image("https://i.imgur.com/Tie664s.jpg")
