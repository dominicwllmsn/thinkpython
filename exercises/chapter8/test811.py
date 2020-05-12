def is_reverse(w1, w2):
	if len(w1) != len(w2):
		return False

	i = 0
	j = len(w2)-1

	while j >= 0: 
		if w1[i] != w2[j]:
			return False
		i += 1
		j -= 1

	return True

print(is_reverse('reppots', 'stopper'))