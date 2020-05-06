def has_no_e(word):
	if not 'e' in word:
		return True
	else:
		return False

def avoids(word, forbidden):
	for c in forbidden:
		if c in word:
			return False
	return True

counter = 0
with open('words.txt') as fin:
	letters = input('Enter the forbidden letters: ')
	for line in fin:
		if avoids(line.strip(), letters):
			counter += 1

	print('Number of words without those letters:',counter)
