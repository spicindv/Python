num_a = 0
print('Для выхода из программы введите q')
while True:
	num_z = list(map(float, input('Введите несколько чисел через пробел: ').split()))
	num_a = sum(num_z) + num_a
	print(num_a)
	spec_sign = input()
	if spec_sign == 'q':
		break
print('end')
