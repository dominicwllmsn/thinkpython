import math

def estimate_pi():
	epsilon = 1e-15
	k = 0
	prefactor = 2*math.sqrt(2)/9801
	series = 0
	while True:
		series += math.factorial(4*k)*(1103+26390*k)/((math.factorial(k)**4)*396**(4*k))
		est = 1/(prefactor*series)
		if abs(est - math.pi) < epsilon:
			return est
		else:
			k += 1	

print(estimate_pi())