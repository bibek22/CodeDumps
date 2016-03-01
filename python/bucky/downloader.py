#!/usr/bin/python
import urllib.request
from html.parser import HTMLParser

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; \
rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) \
Gecko/2009021910 Firefox/3.0.7'}

data = ""


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            

    def handle_data(self, data):
        print(data)


def download_stock_data(url):
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    global data
    data = response.read()


# url = "http://www.brainyquote.com/quotes/topics/topic_valentinesday.html"
url = "https://www.google.com.np/?gws_rd=ssl"
download_stock_data(url)

parser = MyHTMLParser()
parser.feed(data.decode("utf-8"))
