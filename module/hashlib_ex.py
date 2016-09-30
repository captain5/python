#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
python 对字符串数据和文件数据进行MD5、SHA1哈希散列运算
http://www.du52.com/text.php?id=375
'''

__author__ = "wangaibo168@163.com"

import sys;
reload(sys);
sys.setdefaultencoding("utf-8");

data = "abc";
import hashlib;
# 对字符串数据进行MD5哈希
print "字符串MD5 : ",hashlib.md5(data).hexdigest();
# 对文件进行MD5哈希
fp = open('l1.php','rb');
fdata = fp.read();
fp.close();
md5 = hashlib.md5();
md5.update(fdata);
print "文件MD5 : ",md5.hexdigest();
# 对字符串数据进行SHA1哈希
print "字符串SHA1 : ",hashlib.sha1(data).hexdigest();
# 对文件数据进行SHA1哈希
sha1 = hashlib.sha1();
sha1.update(fdata);
print "文件SHA1 : ",sha1.hexdigest();
