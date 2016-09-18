password_list = ['*#*#', '12345']
def account_login():
	password = input('Password:')
	print(type(password))
	password_correct = password == password_list[-1]
	password_reset = password == password_list[0]
	if password_correct:
		print('Login success!')
	elif password_reset:
		new_password = input('Enter a new password:')
		password_list.append(new_password)
		account_login()
		print('Your password has changed sucessfully!')
	else:
		print('Wrong password or invalid input!')
		
		account_login()
account_login()
