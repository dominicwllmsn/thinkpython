import random, time

def nested_sum(t):
	total = 0
	for ele in t:
		total += sum(ele)
	return total

def cumsum(t):
	cum_list = []
	for i in range(len(t)):
		cum_list.append(sum(t[:i+1]))
	return cum_list

def middle(t):
	return t[:][1:-1]

def chop(t):
	t = t[1:-1]
	return None

def is_sorted(t):
	return sorted(t) == t

def is_anagram(s1, s2):
	return sorted(list(s1)) == sorted(list(s2))

def has_duplicates(t):
	t1 = sorted(t)
	for i in range(len(t1)-1):
		if t1[i] == t1[i+1]:
			return True
	return False

def bday_paradox(n):
	dup_count = 0
	for i in range(n):
		t = [random.randint(1,365) for x in range(23)]
		if has_duplicates(t):
			dup_count += 1
	return dup_count/n

def read_file(flag=True):
	t = []
	with open('words.txt') as fin:
		for line in fin:
			if flag == True:
				t.append(line.strip())
			else:
				t += [line.strip()]
	return t

def in_bisect(t, target):
	x = int(len(t)*.5)
	x_low = 0
	x_high = len(t)-1
	i = 0
	target = target.lower()
	while i < 20:
		if target < t[x]:
			x_high = x
		elif target > t[x]:
			x_low = x
		elif target == t[x]:
			return True, x
		x = int(.5*(x_high+x_low))
		i += 1
	return False, -1

def reverse_pair(t):
	word_list = t[:]
	for word in word_list:
		rev_exists, i = in_bisect(word_list, word[::-1])
		if rev_exists:
			print(word, word[::-1])
			word_list.pop(i)

def interlock(word_list, word):
    """Checks whether a word contains two interleaved words.

    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens)[0] and in_bisect(word_list, odds)[0] 

def interlock_general(word_list, word, n=3):
    """Checks whether a word contains n interleaved words.

    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter)[0]:
            return False
    return True
		


t1 = [[1,2],[3],[4,5,6]]
print(nested_sum(t1))

t2 = [1,2,3,4,5,6,7,8,9,10]
print(cumsum(t2))

print(middle(t2))

print(is_sorted(t2))

s1 = 'god'
s2 = 'dog'
print(is_anagram(s1, s2))

print('---')
print(bday_paradox(1000))
print('---')

start_time = time.time()
read_file(flag=True)
elapsed_time = time.time() - start_time
print(elapsed_time, 'flag = True')
start_time = time.time()
read_file(flag=False)
elapsed_time = time.time() - start_time
print(elapsed_time,'flag = False')
print('---')

word_list = read_file()
print(in_bisect(word_list,'CONVULSE'))
print('---')
#reverse_pair(word_list)

for word in word_list:
	if interlock(word_list,word):
		print(word[::2], '&', word[1::2])

for word in word_list:
    if interlock_general(word_list, word, 3):
        print(word, word[0::3], word[1::3], word[2::3])