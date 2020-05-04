def is_power(a, b):
	if a == b:
		return True
	elif a%b:
		return False
	elif not a%b:
		return is_power(a/b, b)
		

print(is_power(20,2))