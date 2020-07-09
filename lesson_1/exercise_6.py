print('Пробежки спортсмена')
a = int(input('Результат первого дня '))
b = int(input('Общий результат составляет не менее '))

i = 1
distance = a
while distance <= b:
    print(f'{i}-й день: {distance:.2f}')
    distance += (distance * 0.1)
    i += 1
print(f'На {i}-й день спортсмен достиг результата - {distance:.2f}')
