# -*- coding:utf-8 -*-
'''
    created by captain9 2017-1-2
'''

__version__ = '0.1'


class Hello(object):
	def hello(self,name):
		u'''please input a name!
		| hello   | xiaoming        | 
		'''
		print 'Hello, ' + name + '!'

	def decode(self,name):
		return customerstr.decode('utf-8')
		
	def sum(self,a,b):
		u'''please input a name!
		| hello   | xiaoming        | 
		'''
		return(a + b)
		
		
if __name__ == "__main__":
    name = u'xiaoming'
    run = Hello()
    run.hello(name)