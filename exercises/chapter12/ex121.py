def most_frequent(s):
	""" Takes string s, prints letters in
	decreasing frequency
	"""
	d = dict()
	for c in s:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1
	print(*sorted(d.items(), key=lambda x: x[1], reverse=True))

def anagrams(word_list):
	d_all = dict()
	for word in word_list:
		letters = tuple(sorted(word))
		if letters not in d_all:
			d_all[letters] = [word]
		else:
			d_all[letters].append(word)

	d_anagrams = dict()
	for key, value in d_all.items():
		if len(value) > 2:
			d_anagrams[key] = value

	return d_anagrams

word_list = []
with open('words.txt') as fin:
	for line in fin:
		word_list.append(line.strip())

#s1 = ''.join(word_list)
#most_frequent(s1)

d = anagrams(word_list)
for val in sorted(d.values(), key=lambda x: len(x), reverse=True):
	if len(val[0]) >= 8:
		print(val)
		break