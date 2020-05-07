import string

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

				t = []
				for ele in line_list:
					if ele != '':
						t.append(ele)
							
				book_list += t
	return book_list, freq_dict

def read_list(file):
	word_dict = {}
	with open(file) as fin:
		for line in fin:
			word_dict[line] = 1
	return word_dict

def compare_text(d1, d2):
	diff = {}
	for k1 in d1:
		if k1 not in d2:
			diff[k1] = None
	return diff

def compare_sets(d1, d2):
	diff = set(d1.keys())-set(d2.keys())
	return diff



if __name__ == '__main__':
	book = 'aainw.txt'
	aainw_list, aainw_freq = read_book(book)
	word_dict = read_list('words.txt')

	#print('Total number of different words:', len(aainw_freq.keys()))
	#print('Most frequently used words:', sorted(aainw_freq.items(), key=lambda x: x[1], reverse = True)[:20])
	print(compare_sets(aainw_freq, word_dict) == set(compare_text(aainw_freq, word_dict)))