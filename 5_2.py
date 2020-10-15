with open('my_file2.txt') as file:
	i = 0
	for line in file:
		str1 = line.split()
		print(f'Количество слов в {i + 1} строке:  {len(str1)}')
		i += 1
print(f'Количество строк в файле: {i}')
