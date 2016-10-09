#!/usr/bin/env python
import pickle

# define class
class Bird(object):
	have_feather = True
	way_of_reproduction = 'egg'

fn = 'a.pkl'
with open(fn, 'rb') as f:
	summer = pickle.load(f)

	
	
