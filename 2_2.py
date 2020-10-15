my_list = []
n = int(input("Введите количество элементов списка: "))
print("Введите поочередно элементы списка через 'enter'")
for i in range(0, n):
    element = input()
    my_list.append(element)
print(f"Ваш список - {my_list}")

even = my_list[::2]
odd = my_list[1::2]

new_my_list = odd + even
print(f"Ваш новый список - {new_my_list}")
