print('Рейтинг')
rate = []
while True:
    new_num = input('Введите число. Для окончания нажмите q ')
    if new_num == 'q':
        break
    while not new_num.isdigit():
        new_num = input('Введите число. Для окончания нажмите q ')
    rate.append(int(new_num))
    print(sorted(rate, reverse=True))
