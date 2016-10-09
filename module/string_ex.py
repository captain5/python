>>> m = "Hello world!"
>>> m.find(H)
>>> m.find('H')
0
>>> m.find('d')
10

str = ’0123456789′
print str[0:3] #截取第一位到第三位的字符

>>> abc = 'Hello world! hi'
>>> abc.split()
['Hello', 'world!', 'hi']

format:
>>> a = 12
>>> b = 'bob'
>>> "{} is {} age old".format(b, a)
'bob is 12 age old'

"{1} is {0} age old".format(a, b)
'bob is 12 age old'
