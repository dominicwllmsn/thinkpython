import anagram_sets, dbm, pickle

def store_anagrams(filename):
	d = anagram_sets.all_anagrams(filename)

	with dbm.open('dictionaries', 'c') as db:
		for word, anagrams in d.items():
			s = pickle.dumps(anagrams)
			db[word] = s

def read_anagrams(word, db):
	try:
		if word in db:
			t = pickle.load(db[word])
			return t
	except:
		print(word, 'not in database.')
		return None

