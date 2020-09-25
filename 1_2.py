sec_in = int(input('Введите время в секундах: '))
hours = sec_in // 600
minutes = (sec_in % 600) // 60
seconds = (sec_in % 600) % 60

# вывод времени в формате чч:мм:сс
print(f"{hours}:{minutes}:{seconds}")
