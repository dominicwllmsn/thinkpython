def sum_all(*args):
	return sum(args)

def has_match(t1, t2):	
	for x, y in zip(t1, t2):
		if x == y:
			return True
	return False

print(sum_all(1,2,3,4,5))
s = 'abc'
t = [0,1,2]
print(list(zip(t,s)))
for pair in zip(t,s):
	print(pair)

for ind, ele in enumerate('special'):
	print(ind, ele)
