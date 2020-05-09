import os

def find_extension(dirname, file_ext):
	file_list = list()
	n = len(file_ext)
	for name in os.listdir(dirname):
		path = os.path.join(dirname,name)

		if os.path.isfile(path) and file_ext in path[-n:]:
			file_list.append(path)
		else:
			find_extension(path)

def get_checksum(path):
	cmd  = 'md5sum ' + path
	fp = os.popen(cmd)
	checksum = fp.read()
	fp.close()
	return checksum

def find_duplicates(file_list):
	d = dict()
	dupes = list()
	for file in file_list:
		checksum = get_checksum(file)
		d[checksum] = d.setdefault(checksum, []).append(file)
	for key, val in d.items():
		if len(val) >= 2:
			dupes.append(val)

	return dupes


