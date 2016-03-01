#!/usr/bin/env python
import urllib.request
import urllib.parse

# x = urllib.request.urlopen('https://www.google.com')
# print(x.read())
'''
url = "http://pythonprogramming.net"
values = {'s': 'basic', 'submit': 'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

print(respData)
'''

try:
    x = urllib.request.urlopen('https://google.com/search?q=test')

    print(x.read())


except Exception as e:
    print(str(e))

try:
    url = 'https://google.com/search?q=test'
    headers = {}
    headers['User-agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0Mozilla/5.0 (X11; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'

    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()

except Exception as e:
    print(str(e))
    
