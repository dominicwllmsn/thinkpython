def rotate_word(word, step):
	val_z = 122
	val_a = 97
	new_word = ''

	for c in word:
		new_value = ord(c.lower()) + step
		if new_value > val_z:
			new_char = chr(val_a + (new_value - val_z))
		elif new_value < val_a:
			new_char = chr(val_z - (val_a - new_value))
		else:
			new_char = chr(new_value)

		if c.isupper(): new_char = new_char.upper()
		new_word += new_char
	return new_word

words_dict = dict()
with open('words.txt') as fin:
	for line in fin:
		words_dict[line.strip()] = True

rotate_pairs = dict()
for key in words_dict:
	for i in range(1,26):
		new_word = rotate_word(key, i)
		if new_word != key and new_word in words_dict:
			rotate_pairs[key] = new_word
print(rotate_pairs)