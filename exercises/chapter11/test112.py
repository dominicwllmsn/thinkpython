def histogram(s):
	d = dict()
	for c in s:
		d[c]= d.get(c, 0) + 1
	return d

def print_sortedhist(h):
	for c in sorted(h):
		print(c, h[c])

def reverse_lookup(d, v):
	for k in d:
		if d[k] == v:
			return k
	raise LookupError('value does not appear in dictionary')

def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse

def fibonacci(n):
	if n in known:
		return known[n]

	res = fibonacci(n-1) + fibonacci(n-2)
	known[n] = res
	return res

if __name__ == '__main__':
	h = histogram('brontosaurus')
	print_sortedhist(h)
	print('---')
	print(reverse_lookup(h, 2))
	print(invert_dict(h))
	print('---')
	known = {0:0, 1:1}
	print(fibonacci(10))
	print(known)