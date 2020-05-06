def consecutive_doubles(word, total):
	i = 0
	doubles = 0
	while i < len(word)-2:
		if doubles >= 3: 
			return True
		if word[i] == word[i+1]:
			doubles += 1
			i += 2
			continue
		i += 1
	return False

with open('words.txt') as fin:
	for line in fin:
		if consecutive_doubles(line.strip(), 3):
			print(line)