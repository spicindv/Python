with open('my_file5.txt', 'w') as f:
	f.write('1 2 3 4 10')
with open('my_file5.txt') as f:
	my_str1 = f.read()
	my_str2 = my_str1.split()
	for i, item in enumerate(my_str2):
		my_str2[i] = int(item)
	sum = 0
	for j in my_str2:
		sum += j
	print(sum)

