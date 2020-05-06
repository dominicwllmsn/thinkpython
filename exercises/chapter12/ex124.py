def remove_one(word):
	children = []
	t = list(word)
	for i in range(len(word)):
		t_copy = t[:]
		del t_copy[i]
		new_word = ''.join(t_copy)

		if new_word in word_dict:
			children.append(new_word)
	return children

def reduce_test(words):
	global reducible
	print(words)
	for c in words:
		print(c)
		if c in reducible:
			reducible += [c]
			return True
		else:
			reduce_test(remove_one(c))
	return False


word_dict = {}
with open('words.txt') as fin:
	for line in fin:
		word_dict[line.strip()] = True

word_dict[''] = True
word_dict['a'] = True
word_dict['i'] = True

reducible = ['', 'a', 'i']

print(reduce_test(['sprite']))
