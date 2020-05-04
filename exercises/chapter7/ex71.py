import math

def mysqrt(a):
	epsilon = 0.000001
	x = a/2
	while True:
		y = (x + a/x)/2
		if abs(y-x) < epsilon:
			return y
		else:
			x = y

def test_square_root(n):
	print('a', 'mysqrt(a)', 'math.sqrt(a)', 'diff', sep=' '*4)
	print('_', '_________', '____________', '____', sep=' '*4)
	for a in range(1, n+1):
		est = mysqrt(a)
		actual = math.sqrt(a)
		diff = abs(est-actual)
		print('{:}    {:f}    {:f}    {:f}'.format(a, est, actual, diff))


test_square_root(10)