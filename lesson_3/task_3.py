
# Реализовать функцию my_func(), 
# которая принимает три позиционных аргумента, 
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    tmp = sorted([a, b, c], reverse=True)
    return tmp[0] + tmp[1]

print(my_func(2, 6, 1))
print(my_func(1, 2, 3))
