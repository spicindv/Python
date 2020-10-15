my_list = [5, 7, 2, 23, 7, 1, 5, 9, 4]
new_list = [num for i, num in enumerate(my_list) if my_list[i] > my_list[i - 1] and i != 0]
print(new_list)
