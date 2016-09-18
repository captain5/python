#!/usr/bin/python
#_*_ coding:utf-8 _*_
import os
#os.system('ls')
def text_create(name, msg):
	#cur_path = '/Users/apple/Desktop/'
	cur_path = ''
	full_path = cur_path + name + '.txt'
	file = open(full_path, 'w')
	file.write(msg)
	file.close()
	#print('Done')

text_create('Hello', 'Hello world!')
'''
def text_filter(word, censored_word = 'lame', change_word = 'Awesome'):
	return word.replace(censored_word, change_word)

#print(text_filter('Python is lame!'))

def censored_text_create(name, msg):
	clean_msg = text_filter(msg)
	text_create(name, clean_msg)

censored_text_create('Try', 'lame!lame!lame!')
'''
