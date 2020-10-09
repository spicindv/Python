print('Введите данные в файл через enter')
with open('my_file1.txt', 'w') as f:
	while True:
		my_str = input()
		for line in my_str:
			f.write(line + '\n')
		if my_str == '':
			break
