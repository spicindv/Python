rev = int(input('Введите значение выручки: '))
cost = int(input('Введите значение издержек: '))
if rev > cost:
	print('Фирма отработала с прибылью')
	profit_ab = rev / cost
	profit = rev - cost
	print('Рентабельность выручки: ' + str(profit_ab))
	number_of_employees = int(input('Введите численность сотрудников фирмы: '))
	profit_1 = profit / number_of_employees
	print('Прибыль на одного сотрудника составила: ' + str(profit_1))
else:
	print('Фирма несет убытки')
