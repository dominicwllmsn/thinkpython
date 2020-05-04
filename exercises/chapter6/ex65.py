def gcd(a, b):
	r = a%b
	if r == 0:
		return b
	else:
		return gcd(b, r)

print(gcd(864,42))