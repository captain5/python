y = 10
def guess(y):
	x = input('Start guess:')
	if x > y:
		print('Big than')
		guess(y)
	elif x < y:
		print('Little than')
		guess(y)
	elif x == y:
		print('Congratulation!')
	else:
		print('Wrong!')	
guess(y)
