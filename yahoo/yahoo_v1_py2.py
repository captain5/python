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
from bs4 import BeautifulSoup

def Gethtml():
    #values={'user_name':'80945763@qq.com', 'pass_word':'xinxin'}
    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:53.0) Gecko/20100101 Firefox/53.0"
    referer = "https://finance.yahoo.com/"
    headers={"User-agent":user_agent,'referer':referer}
    url="https://finance.yahoo.com/quote/1810.HK?p=1810.HK&.tsrc=fin-srch-v1"
    #data=urllib.parse.urlencode(values)   
    #注意只是针对values进行了解码，而headers没有。
    #bianary_data=data.encode('utf-8')
    req=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(req,timeout=10)
    #print (response.read())
    return response.read()
    #print(response.geturl())

html = Gethtml()

#print html
#reg = r'([0-9]{2}\.[0-9]{3})'

#reg = r'([2]{1}[0]{1}\.[0-9]{3})'
#i = re.compile(reg)
#r = re.findall(i, html)
#print(r)


#r = re.search(i, html)
#print("ERUUSD:\nCur   |   Open   |  Yesterday  |  Low  |  High")
#print("--------------------")

#print(r.groups())

def send_move():
    print("begein send_move")
    # nickname = input('please input your firends\' nickname : ' )
    #   想给谁发信息，先查找到这个朋友,name后填微信备注即可,deepin测试成功
    # users = itchat.search_friends(name=nickname)
    users = itchat.search_friends(name='Captain')   # 使用备注名来查找实际用户名
    #获取好友全部信息,返回一个列表,列表内是一个字典
    print(users)
    #获取`UserName`,用于发送消息
    userName = users[0]['UserName']
    print userName
    itchat.send("该起来动一下了！",toUserName = userName)
    print('succeed')

soup = BeautifulSoup(html, 'lxml')
c = soup.find_all('span')[19].string
print c
c1 = float(c)
if c 