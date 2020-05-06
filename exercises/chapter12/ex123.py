def metathesis_pair(word_list):
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
	
	meta_list = []
	for t in d_anagrams.values():
		for s1 in t:
			for s2 in t:
				counter = 0
				if s1 != s2:
					for i in range(len(s1)):
						if s1[i] != s2[i]:
							counter += 1
						if counter > 2:
							break
					if counter == 2:
						meta_list.append((s1,s2))
	return meta_list


word_list = []
with open('words.txt') as fin:
	for line in fin:
		word_list.append(line.strip())

meta_list = metathesis_pair(word_list)
print(meta_list)
