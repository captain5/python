#coding:utf-8
'''
urllib.request.urlopen() function in Python 3 is equivalent to urllib2.urlopen()
urllib.request.Request() function in Python 3 is equivalent to urllib2.Request()
'''
#python3
#import urllib.request
#import urllib.parse
#python2
import urllib
import urllib2
import re
import sys

def Gethtml(url, referer):
    #values={'user_name':'80945763@qq.com', 'pass_word':'xinxin'}
    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:53.0) Gecko/20100101 Firefox/53.0"
    #referer = "http://quote.forex.hexun.com/forexdata2010.htm"
    headers={"User-agent":user_agent,'referer':referer}
    #url="http://quote.forex.hexun.com/EURUSD.shtml"
    #data=urllib.parse.urlencode(values)   
    #注意只是针对values进行了解码，而headers没有。
    #bianary_data=data.encode('utf-8')
    req=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(req,timeout=10)
    #print (response.read())
    return response.read()
    #print(20*"*")
    #print(response.geturl())


hexun = {'url':'http://quote.forex.hexun.com/EURUSD.shtml','referer':'http://quote.forex.hexun.com/forexdata2010.htm'}
fx678 = {'url':'http://quote.fx678.com/exchange/WH','referer':'http://www.fx678.com/'}
#print(sys.argv)
if len(sys.argv)<=1:
    wh = hexun
else:
    wh = fx678
html = Gethtml(wh['url'],wh['referer'])
if wh == hexun:
    reg = r'([0-1]{1}\.[0-9]{4})'
    i = re.compile(reg)
    r = re.findall(i, html)
    print("hexun ERUUSD:\nCur   |     Open |  Yesterday  |  Low  |  High")
    print(r)
else:
    reg = r'([0-1]{1}\.[0-9]{4})'
    i = re.compile(reg)
    r = re.findall(i, html)
    #print(r)
    print("fx678 ERUUSD:\nCur   |     Open |  Yesterday  |  Low  |  High")
    print(r[1],r[3],r[6],r[5],r[4])