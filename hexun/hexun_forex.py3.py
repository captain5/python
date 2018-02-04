#coding:utf-8
'''
urllib.request.urlopen() function in Python 3 is equivalent to urllib2.urlopen() in Python2
urllib.request.Request() function in Python 3 is equivalent to urllib2.Request() in Python2
'''
#python3.5
import urllib.request
#python2.7
#import urllib
#import urllib2

import re


def Gethtml(url, referer):
    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:53.0) Gecko/20100101 Firefox/53.0"
    headers={"User-agent":user_agent,'referer':referer}
    #python3.5
    req=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(req,timeout=10)
    #python2.7
    #req=urllib2.Request(url,headers=headers)
    #response=urllib2.urlopen(req,timeout=10)
    return response.read()

url=referer="http://quote.forex.hexun.com/EURUSD.shtml"
html = str(Gethtml(url, referer))
reg = r'([0-1]{1}\.[0-9]{4})'
i = re.compile(reg)
r = re.findall(i, html)
print("Hexun ERUUSD:\nCur   |     Open |  Yesterday  |  Low  |  High")
print(r)