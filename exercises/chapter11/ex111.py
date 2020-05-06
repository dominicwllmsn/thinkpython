import time

def file_to_dict(t):
	d = dict()
	for ele in t:
		d[ele] = 0
	return d

def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		inverse.setdefault(val, []).append(key)
	return inverse

words_list = []
with open('words.txt') as fin:
		for line in fin:
			words_list.append(line.strip())

words_dict = file_to_dict(words_list)

start = time.time()
print('bookkeeping' in words_list)
interval = time.time() - start
print(interval)

start = time.time()
print('bookkeeping' in words_dict)
interval = time.time() - start
print(interval)

d1 = {'a':1, 'b':2, 'c':1}
print(invert_dict(d1))