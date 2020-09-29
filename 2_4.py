my_str = input('Введите несколько слов через пробел: ')
my_list = my_str.split()

i = 0
for el in my_list:
	i += 1
	print(f'{i} : {el}')
