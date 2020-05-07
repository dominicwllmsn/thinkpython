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
				print(maintext)
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

book = 'aainw.txt'
word_list, freq_dict = read_book(book)

print('Total number of different words:', len(freq_dict.keys()))

print('Most frequently used words:', sorted(freq_dict.items(), key=lambda x: x[1], reverse = True)[:20])