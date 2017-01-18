# -*- coding:utf-8 -*-
'''
    created by captain9 2017-1-2
'''

__version__ = '0.1'


class Hello(object):
	def hi(self,name):
		u'''接收一个名字，并问候.例如
		| hi  | xiaoming        | 
		'''
		print 'Hello, ' + name + '!'

	def decode(self,name):
		return customerstr.decode('utf-8')

if __name__ == "__main__":
    name = u'xiaodong'
    run = Hello()
    run.hi(name)
