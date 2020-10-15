a = float(input('Введите результат первого дня пробега: '))
b = float(input('Введите желаемый результат спортсмена: '))
day = 1
print(f"{day}-й день:  {round(a, 2)}")
while b >= a:
	day += 1
	a = a + 0.1*a
	print(f"{day}-й день:  {round(a, 2)}")
