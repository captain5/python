#coding=utf-8

#urllib模块提供了读取Web页面数据的接口
import urllib
#re模块主要包含了正则表达式
import re
#定义一个getHtml()函数
def getHtml(url):
    page = urllib.urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    html = page.read() #read()方法用于读取URL上的数据
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'    #正则表达式，得到图片地址,两个双引号也是要匹配的内容
	#src="http://imgsrc.baidu.com/forum/w%3D580/sign=a2508e37d11b0ef46ce89856edc551a1/6d0e3a292df5e0fe9fb74f185f6034a85edf7209.jpg" pic_ext="jpeg"
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 1
    #print imglist
    for imgurl in imglist:
		urllib.urlretrieve(imgurl,'F:/tmp\%s.jpg' % x)
		x+=1
		#定义获取几张图片
		if x == 8:
			return "Done!"

html = getHtml("http://tieba.baidu.com/p/3279995608")
print getImg(html)
