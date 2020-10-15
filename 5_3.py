with open('my_file3.txt', encoding='utf-8') as f:
	for line in f:
		st = line.split()
		st_fl = float(st[1])
		if st_fl < 20000:
			print(st[0])
