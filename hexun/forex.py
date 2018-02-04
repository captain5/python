#coding:utf-8
#python3
import urllib2
import urllib
import re

html = urllib.urlopen('forex.hexun.com').read()
#print html

reg = r'>([0-9]{3}\.[0-9]{4})</td>'
i = re.compile(reg)
r = re.findall(i, html)
print("Sell:", r[3])