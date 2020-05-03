def check_fermat(a, b, c, n):
	if n > 2 and a**n + b**n == c**n:
		print('Fermat was wrong!')
	else:
		print("No, that doesn't work.")

a = int(input('Value of a:\n'))
b = int(input('Value of b:\n'))
c = int(input('Value of c:\n'))
n = int(input('Value of n:\n'))

check_fermat(a, b, c, n)