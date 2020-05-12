def binomial_coeff(n, k):
	"""Compute the binomial coefficient "n choose k".
	n: number of trials
	k: number of successes
	returns: int
	"""
	if (n, k) in b_coeff:
		return b_coeff[(n, k)]

	if k == 0:
		return 1
	if n == 0:
		return 0

	res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
	b_coeff[(n, k)] = res
	return res

b_coeff = {}

print(binomial_coeff(15, 4))
print(b_coeff)