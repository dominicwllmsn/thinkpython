def eval_loop():
	result = None
	while True:
		string = input('Please input the expression: ')
		if string == 'done':
			print('Done!')
			return result
		result = eval(string)
		print(result)

eval_loop()