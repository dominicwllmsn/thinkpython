def sed(pat, rep, fi1, fi2):
	whitespace = ['\n', '\r', '\t']
	try:
		fin = open(fi1, 'r')
		fout = open(fi2, 'w')
	except:
		print("Could not open", fi1, "- exiting.")
		return False
	try:
		for line in fin:
			line_list = split(line)
			for i, ele in enumerate(line_list):
				if pat in ele:
					if  ele[-2:] in whitespace:
						s_write = rep+ele[-2:]
					else:
						s_write = rep
				else:
					continue
				line_list[i] = s_write
			fout.write(' '.join(line_list))

		fin.close()
		fout.close()
		return True
	except:
		print("Error in reading/writing")
		return False

