# -*- coding: utf-8 -*-
'''
练习

请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax2 + bx + c = 0

的两个解。

提示：计算平方根可以调用math.sqrt()函数：

>>> import math
>>> math.sqrt(2)
1.4142135623730951
'''

import math

def quadratic(a, b, c):
	
	for s in (a,b,c):
		if not isinstance(s,(int,float)):
			raise TypeError("Input Error!")			
	if a!=0:
		delta = b*b-4*a*c
		if delta>=0:
			return (-b+math.sqrt(delta))/2*a, (-b-math.sqrt(delta))/2*a
		else:
			return "no real root"
	else:
		return "input error ,a can't be zero!"
print(quadratic(2, 3, 1))	
print(quadratic(5, 3, 1))	
print(quadratic('A', 3, 1))		