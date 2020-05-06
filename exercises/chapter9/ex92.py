def has_no_e(word):
	if not 'e' in word:
		return True
	else:
		return False

counter = 0
no_e = 0
with open('words.txt') as fin:
	for line in fin:
		counter += 1
		if has_no_e(line.strip()):
			print(line)
			no_e += 1

	print('Percentage of no_e: ',no_e*100/counter,'%',sep='')
