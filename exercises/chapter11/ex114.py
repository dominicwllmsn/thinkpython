def has_duplicates(t):
	d = dict()
	for ele in t:
		if ele in d:
			return True
		d[ele] = True
	return False
