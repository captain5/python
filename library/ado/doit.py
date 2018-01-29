# -*- coding:utf-8 -*-
'''
    created by captain9 2017-1-2
'''

__version__ = '0.1'


class HelloMan(object):
	def helloa(self,name):
		u'''please input a name!
		| hello   | xiaoming        | 
		'''
		print 'Hello, ' + name + '!'

	def decodea(self,name):
		return customerstr.decode('utf-8')

if __name__ == "__main__":
    name = u'xiaoming'
    run = Hello()
    run.hello(name)