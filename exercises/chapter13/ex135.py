import random

def histogram(t):
	hist = dict()
	for x in t:
		hist[x] = hist.setdefault(x, 0) + 1
	return hist

def choose_from_hist1(h):
	pop = list(h.keys())
	weights = list(h.values())
	return random.choices(pop, weights)

def choose_from_hist2(h):
	t = []
	for word, freq in h.items():
		t.extend([word] * freq)
	return random.choice(t)


t = [0,1,2,3,4,5,6,7,8,9,0,2,3,4,5,6,4,4,4,4,4,4,3]
for i in range(10):
	x = random.random()
	y = random.randint(1,10)
	print(x,y,random.choice(t))

h = histogram(t)
print(choose_from_hist2(h))