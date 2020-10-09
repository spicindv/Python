with open('my_file4.txt') as f:
	for line in f:
		if 'One' in line:
			line.replace('One', 'Один')
		if 'Two' in line:
			line.replace('Two', 'Два')
		if 'Three' in line:
			line.replace('Three', 'Три')
		if 'Four' in line:
			line.replace('Four', 'Четыре')
		print(line)

