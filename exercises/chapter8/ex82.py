def is_palindrome(word):
	return word == word[::-1]

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



word = 'banana'
letter = 'a'

print(word.count(letter))

print(rotate_word('IbM',-1))