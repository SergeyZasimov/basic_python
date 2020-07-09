print('Наибольшая цифра в числе')
num = int(input('Введите число '))
max_n = 0
while num:
    current_n = num % 10
    if current_n > max_n:
        max_n = current_n
    num //= 10
print('Наибольшая цифра', max_n)
