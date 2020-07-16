
def division(a, b):
    while b == 0:
        print('Деление на ноль')
        b = check_num('второе')
    return f'{a} / {b} =  {(a / b):.2f}'
    
def check_num(description):
    num = input(f'Введите {description} число ')
    while num.isalpha():
        num = input(f'Введите {description} число ')
    return int(num)

a = check_num('первое')
b = check_num('второе')
print(division(a, b))
