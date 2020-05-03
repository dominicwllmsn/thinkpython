def do_n(f, n):
	if n <= 0:
		return
	else:
		f()
		do_n(f, n-1)

def func():
	print(s)

s = input('Type a word:\n')
do_n(func, 5)

