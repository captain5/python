#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import pickle

# define class
class Bird(object):
	have_feather = True
	way_of_reproduction = 'egg'

summer = Bird()
fn = 'a.pkl'
with open(fn, 'wb') as f:
	picklestring = pickle.dump(summer, f)

	
	
