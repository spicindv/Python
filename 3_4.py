# Первое решение
# def my_func(x, y):
#     y = abs(y)
#     return 1 / (x**y)
#
#
# print(my_func(4, - 2))

# Второе решение
def my_func(x, y):

    while y < -1:
        x *= x
        y += 1
    return 1 / x


print(my_func(4, - 2))
