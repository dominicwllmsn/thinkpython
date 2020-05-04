def find (word, letter, start = 0):
	index = start
	while index < len(word):
		if word[index] == letter:
			return index
		index += 1
	return -1

def count(word, letter):
	counter = 0
	index = 0
	while index < len(word):
		index = find(word, letter, index)
		if index != -1:
			counter += 1
			index += 1
			continue
		else:
			return counter
	return counter


print(count('banana', 'n'))