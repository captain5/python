#-*-coding:utf8-*-
import itchat
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
import time 

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
from bs4 import BeautifulSoup

def Gethtml(url):
    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:53.0) Gecko/20100101 Firefox/53.0"
    referer = "https://finance.yahoo.com/"
    headers={"User-agent":user_agent,'referer':referer}
    req=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(req,timeout=10)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')    
    c = float(soup.select('span[data-reactid="35"]')[0].string)     # list Tag  string int
    # print type(current[0]) #<class 'bs4.element.Tag'>
    #print c  
    o = float(soup.select('span[data-reactid="48"]')[1].string)
    #print(type(open[1]))  Tag
    #print o
    # <td class="Ta(end) Fw(b) Lh(14px)" data-test="DAYS_RANGE-value">22.02 - 23.49</td>
    day_range_value = soup.select('td[data-test="DAYS_RANGE-value"]')[0].string
    low, high = day_range_value.split('-')
    #print type(low),type(high)  #<type 'unicode'> <type 'unicode'>
    l = float(low)
    h = float(high)
    return o, c, l, h
    
def send_move(msg):
    users = itchat.search_friends(name='Captain')   # 使用备注名来查找实际用户名
    #获取好友全部信息,返回一个列表,列表内是一个字典
    #print(users)
    #获取`UserName`,用于发送消息
    userName = users[0]['UserName']
    #print userName
    itchat.send(msg,toUserName = userName)
    print('succeed')

def crond_a():
    while True:
        o, c, l, h = Gethtml(mi)
        print "open current low high"
        print o, c, l, h
        if h - c < 0.3 :
            print("sale")
            msg = "sale"
            #send_move(msg)
        elif c - l < 0.3:
            print("buy")
            msg = "buy"
            #send_move(msg)
        print("sleep 15 seconds")
        time.sleep(15)
def crond_b():
    while True:
        o, c, l, h = Gethtml(url)
        print "open current low high"
        print o, c, l, h
        if c > 18.95 :
            print("sale")
            msg = "sale"
            send_move(msg)
        elif c < 18.45:
            print("buy")
            msg = "buy"
            send_move(msg)
        print("sleep 20 seconds")
        time.sleep(20)

if __name__=='__main__':
    #itchat.auto_login(hotReload=True)  # 首次扫描登录后后续自动登录
    mi = 'https://finance.yahoo.com/quote/1810.HK?p=1810.HK&.tsrc=fin-srch-v1'
    vank = 'https://finance.yahoo.com/quote/000002.SZ?p=000002.SZ&.tsrc=fin-srch-v1'
    
    if len(sys.argv) < 2: 
        url = mi
    elif sys.argv[1] == "v":
        url = vank
    elif sys.argv[1] == "a":
        url = mi
        crond_b
    elif sys.argv[1] == "b":
        url = mi
        crond_b
    else:
        url = mi
    try:
        o, c, l, h = Gethtml(url)
        print "open current low high"
        print o, c, l, h
    except Exception,KeyboardInterrupt:
        print("Error")

    
    
