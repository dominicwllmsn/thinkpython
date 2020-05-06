def uses_all(word, letters):
	if len(word) < len(letters): 
		return False
	
	occur = 0
	for c in word:
		if not c in letters:
			return False
		else:
			occur += 1
			continue
	result = True if occur >= len(letters) else False
	return result  
	

with open('words.txt') as fin:
	for line in fin:
		if uses_all(line.strip(), 'acefhlo'):
			print(line)
