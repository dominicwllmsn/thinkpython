def right_justify(s):
	length = len(s)
	final = ' '*(70-length)+s
	print(final)

def print_twice(s):
	print(s)
	print(s)

def print_spam():
	print('spam')

def do_twice(f, val):
	f(val)
	f(val)

def do_four(f, val):
	do_twice(f, val)
	do_twice(f, val)

do_four(print, 'spam')
