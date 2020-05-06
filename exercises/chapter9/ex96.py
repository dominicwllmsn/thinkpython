def is_abecedarian(word):
	prev_val = ord('a')
	for c in word:
		if ord(c) >= prev_val:
			continue
		else:
			return False
	return True

counter = 0

with open('words.txt') as fin:
	for line in fin:
		if is_abecedarian(line.strip()):
			counter += 1

print('Total number of abecedarian words:', counter)