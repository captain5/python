#-*-coding:utf8-*-

import urllib,urllib2
import json
import pandas as pd
import re
import time

import itchat
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

def get_dq(code='00005',mkt='AUTO', bgdate='2018-07-9',eddate='2018-07-30',fq=None):

    if mkt=='AUTO':
        if re.search('^\d{5}$',code):
            mkt='hk'
        elif re.search('^6\d{5}$',code):
            mkt='sh'
        elif re.search('^0|3\d{5}$',code):
            mkt='sz'
    code_par= mkt +code
    print 'get dq of %s.%s[from:%s, to:%s]' % (code, mkt, bgdate,eddate)
    if fq==None:
        url= 'http://web.ifzq.gtimg.cn/appstock/app/kline/kline?_var=kline_day&param=%s,day,%s,%s,640,' % (code_par, bgdate,eddate)
        dataname='day'
    else:
        assert fq in ['qfq','hfq']
        url= 'http://web.ifzq.gtimg.cn/appstock/app/hkfqkline/get?_var=kline_day&param=%s,day,%s,%s,640,%s' % (code_par, bgdate,eddate, fq)
        dataname= fq+ 'day'
    cn=urllib.urlopen(url)
    raw='\n'.join(cn.readlines())
    js= re.search('(?<=kline_day=).*$', raw).group()
    jsparsed=json.loads(js)
    dq=pd.DataFrame(jsparsed['data'][code_par][dataname])
    if dq.shape[1]==6:
        dq.columns=  ['date','o','c','h','l','v']
    elif dq.shape[1]==7:
        dq.columns=  ['date','o','c','h','l','v','qy']
    c = dq.iat[-1,2]
    h = dq.iat[-1,3]
    l = dq.iat[-1,4]

    return dq,c,h,l
    # get last line 3 columns
    # dq.iat[-1,2]
    #reload(ab)

def send_move():
    # nickname = input('please input your firends\' nickname : ' )
    #   想给谁发信息，先查找到这个朋友,name后填微信备注即可,deepin测试成功
    # users = itchat.search_friends(name=nickname)
    users = itchat.search_friends(name='Captain')   # 使用备注名来查找实际用户名
    #获取好友全部信息,返回一个列表,列表内是一个字典
    #print(users)
    #获取`UserName`,用于发送消息
    userName = users[0]['UserName']
    #print userName
    itchat.send("该起来动一下了！",toUserName = userName)
    print('succeed')
    
    
if __name__=='__main__':    
    #itchat.auto_login(hotReload=True)  # 首次扫描登录后后续自动登录
    dq,c,h,l = get_dq('01810')
    print get_dq('000002')
    #print get_dq('00002')
    #print(dq.tail(2))
    '''
    while True:    
        dq,c,h,l = get_dq('01810')
        print(dq.tail(2))
        if float(h) - float(c) < 0.3 or float(c) - float(l) < 0.3:
            send_move()
        print("sleep 5 seconds")
        time.sleep(5)

    #wanke
    #print get_dq('000002')   
    '''

    
    