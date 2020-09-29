seasons = ['зима', 'весна', 'лето', 'осень']
num_m = int(input('Введите целое число от 1 до 12: '))
month_dict = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

if num_m > 0 and num_m <= 2 or num_m == 12:
	print(f'Ваш сезон: {seasons[0]}')
elif num_m >= 3 and num_m <= 5:
	print(f'Ваш сезон: {seasons[1]}')
elif num_m >= 6 and num_m <= 8:
	print(f'Ваш сезон: {seasons[2]}')
else:
	print(f'Ваш сезон: {seasons[3]}')

# Вывод для словаря
# print(f'Ваш месяц: {month_dict.values(num_m)}')
print(month_dict.values(num_m))
