from functools import reduce

def mul_list(n1, n2):
    return n1 * n2

my_list = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(mul_list, my_list))
