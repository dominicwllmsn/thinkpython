import dbm, pickle

db = dbm.open('captions', 'c')
# dbm keys and values have to be strings or bytes
# pickle translates objects to a suitable string for a db
# and vice versa
db['test1.png'] = 'test photo 1'
db['test2.png'] = 'test photo 2'
db['test3.png'] = 'test photo 3'
print(db['test1.png'])

for key in db:
	print(key, db[key])

db.close()

t1 = [1, 2, 3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
print(t2)
print(t1 == t2, t1 is t2)
# Hence pickling and unpickling = copying an object
# So can use pickle to store non-strings in a db