import os

def walk(dirname):
	for name in os.listdir(dirname):
		path = os.path.join(dirname,name)

		if os.path.isfile(path):
			print(path)
		else:
			walk(path)

cwd = os.getcwd()

abs_path = os.path.abspath('aainw.txt')
print(abs_path)
print(os.path.exists('emma.txt'))
print(os.path.isdir('C:\\Users\\apost'))
print(os.path.isfile('output.txt'))
#print(os.listdir(cwd))
walk('C:\\Users\\apost\\Documents\\_Coding')
print('---')
for root, dirs, files in os.walk('C:\\Users\\apost\\Documents\\_Coding'):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

fout = open('output.txt', 'w')

line1 = "This is line one."
line2 = "The is the second line."
fout.write(line1)
fout.write(line2)

fout.close()