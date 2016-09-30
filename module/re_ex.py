>>> import re
>>> m = re.search("output_(\d{4})", "output_1986.txt")
>>> print(m.group(1))
1986
>>> print(m.group(0))
output_1986

# res is a string
>>> res
'{"url":"/cgi-bin/luci/;stok=c9ec12465cd921116fa7e7dc01d45832/web/home","token":"c9ec12465cd921116fa7e7dc01d45832","code":0}'
>>> re.search('url":"(.*)","token',res).group(1)
'/cgi-bin/luci/;stok=c9ec12465cd921116fa7e7dc01d45832/web/home'
>>> res[0]
'{'
>>> res[65:69]
'home'

>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
'def'
