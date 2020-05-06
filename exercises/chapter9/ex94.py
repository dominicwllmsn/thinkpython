def uses_only(word, letters):
	for c in word:
		if not c in letters:
			return False
	return True

with open('words.txt') as fin:
	for line in fin:
		if uses_only(line.strip(), 'acefhlo'):
			print(line)
