def division(x, y):
    if y == 0:
        return print('division by zero - error')
    return x / y


x = float(input('Введите х: '))
y = float(input('Введите y: '))
div = division(x, y)
print(div)
