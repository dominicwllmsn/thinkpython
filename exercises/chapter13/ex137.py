import string, random

def key_value_list(h):
	return list(h.keys()), list(h.values())

def bisect_search(target, t):
	x_high = len(t)
	x_low = 0
	x = int(.5*(x_high+x_low))
	for i in range(20):
		x = int(.5*(x_high+x_low))
		if target > t[x]:
			x_low = x
			continue
		elif target < t[x]:
			x_high = x
			continue
		elif target == t[x]:
			return x
	return x

def random_word(h):
	words, freqs = key_value_list(h)
	n = sum(freqs)
	c = []
	for i in range(1, len(freqs)+1):
		c.append(sum(freqs[:i]))
	print(c[-1], len(c), n, len(freqs))
	r = random.randint(1,n)
	index = bisect_search(r, c)
	return words[index]

def read_book(file):
	with open(file) as fin:
		book_list = []
		freq_dict = {}
		maintext = False
		for line in fin:
			line_list = []
			no_punc = ''

			if "*** START OF THIS PROJECT GUTENBERG EBOOK" in line:
				maintext = True
				continue

			if "*** END OF THIS PROJECT GUTENBERG EBOOK" in line:
				break

			if maintext:
				for c in line.strip(string.punctuation+string.whitespace):
					if c in string.punctuation:
						continue
					else:
						no_punc += c.lower()
				if no_punc == '':
					continue
				line_list = no_punc.split(' ')

				for word in line_list:
					freq_dict[word] = freq_dict.setdefault(word, 0) + 1

				book_list += line_list
	return book_list, freq_dict

if __name__ == '__main__':
	book = 'aainw.txt'
	word_list, freq_dict = read_book(book)
	print(random_word(freq_dict))