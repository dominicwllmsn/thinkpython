import string, random

def markov_analysis(word_list, n):
	""" n is prefix length
	"""
	map_dict = dict()
	for i in range(len(word_list)-n):
		prefix = ''
		for j in range(n):
			if j > 0:
				prefix += ' '
			prefix += word_list[i+j]
		suffix = word_list[i+j+1]
		map_dict[prefix] = map_dict.get(prefix, tuple()) + (suffix,)
	return map_dict

def markov_generator(word_list, n, total):
	""" total is minimum generated string length, n is prefix length
	"""
	d = markov_analysis(word_list, n)
	s = ''
	prefixes = tuple(d.keys())
	while len(s.split(' ')) < total:
		if s == '':
			while True:
				start = random.choice(prefixes)
				if start[0].isupper() and start[-1] not in '.";':
					break
			s += start 
		else:
			if '  ' in s[-2]:
				s = s[:-1]
			s_prefix = ' '.join(s.split(' ')[-n:])
			suffixes = d[s_prefix]
			s_addition = random.choice(suffixes)
			s += ' ' + s_addition
	while True:
		if s[-1] in '."' and s[-2] not in 'rs':
			break
		s_prefix = ' '.join(s.split(' ')[-n:])
		suffixes = d[s_prefix]
		s_addition = random.choice(suffixes)
		s += ' ' + s_addition

	return s


def read_book(file, keep_punc=False):
	with open(file) as fin:
		book_list = []
		maintext = False
		for line in fin:
			line_list = []
			s = ''

			if "*END*THE SMALL PRINT!" in line or 'CHAPTER I. Down the Rabbit-Hole' in line:
				maintext = True
				continue
			if "CHAPTER" in line or "VOLUME" in line:
				continue
			if "End of The Project Gutenberg" in line:
				break

			if maintext:
				if keep_punc == True:
					for c in line.strip():
						if c == '-':
							s += ' '
						else:
							s += c
					if s == '':
						continue
					line_list = s.split(' ')

					book_list += line_list
				else:
					for c in line.strip(string.punctuation+string.whitespace):
						if c == '-':
							s += ' '
						if c in string.punctuation:
							continue
						else:
							s += c.lower()
					if s == '':
						continue
					line_list = s.split(' ')

					t = []
					for ele in line_list:
						if ele != '':
							t.append(ele)
							
					book_list += t
	return book_list

book1 = 'emma.txt'
book2 = 'aainw.txt'
word_list1 = read_book(book1, keep_punc=True)
word_list2 = read_book(book2, keep_punc=True)
word_list_all = word_list1 + word_list2

print(markov_generator(word_list_all, n=2, total=20))