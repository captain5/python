#!/usr/bin/env python
# _*_ coding: utf-8 _*_

#if copy code must remember Quotes
#下面的程序会每隔5秒显示当前的日期和时间
import time

print '*** 如果想停止该程序，可以"ctrl" + "C" 退出 ***'
while True:
    ### 显示当前的日期和时间
    print "当前的日期 & 时间 " + time.strftime("%c")
    #### 延迟5秒执行 ####
    time.sleep(5)

