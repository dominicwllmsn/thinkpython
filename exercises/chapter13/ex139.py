import string, math
import matplotlib.pyplot as plt

def zipf_test(t):
	"""t is list of (word, freq) (reverse) sorted by frequency
	"""
	logf_vals = list()
	logr_vals = list()
	for r, word_tuple in enumerate(t):
		word, freq = word_tuple
		logf = math.log10(freq)
		logr = math.log10(r+1)
		logf_vals.append(logf)
		logr_vals.append(logr)
    
	plt.plot(logf_vals, logr_vals)
	plt.show



def read_book(file, keep_punc=False):
	with open(file) as fin:
		book_list = []
		freq_dict = {}
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
						freq_dict[ele] = freq_dict.setdefault(ele, 0) + 1
						t.append(ele)

				book_list += t
	return book_list, sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

book = 'emma.txt'
word_list, freq_dict = read_book(book)

#print(freq_dict[:10])
zipf_test(freq_dict)