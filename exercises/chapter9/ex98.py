def palindromic(word):
	return word == word[::-1]

for miles in range(100000,999999):
	if palindromic(str(miles)[-4:]) and palindromic(str(miles+1)[-5:]) and palindromic(str(miles+2)[-5:-1]):
		print(miles, miles+1, miles+2)