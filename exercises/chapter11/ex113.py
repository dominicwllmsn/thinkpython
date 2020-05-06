def A(m, n):
	if (m, n) in known:
		return known[(m, n)]
	if m == 0:
		known[(m_i, n_i)] = n+1
		return n+1
	elif m > 0 and n == 0:
		return A(m-1, 1)
	elif m > 0 and n > 0:
		return A(m-1, A(m, n-1))

known = dict()

for m in range(4):
	m_i = m
	for n in range(7):
		n_i = n
		print(m_i, n_i, ':', A(m, n))
print(known)
