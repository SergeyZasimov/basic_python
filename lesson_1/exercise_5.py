print('Выручка и издержки фирмы')
gain = int(input('Введите значение выручки '))
charge = int(input('Введите значение издержек '))
profit = gain - charge
if profit > 0:
    print('Фирма работает с прибылью!!!')
    
    rent = (profit / gain) * 100
    print(f'Рентабельность {rent}%')
    
    employeers = int(input('Введите количество сотрудников '))
    employeer_profit = profit / employeers
    print(f'Прибыль на одного сотрудника {employeer_profit}')
    
elif profit < 0:
    print('Фирма работает в убыток :-(')
    
else:
    print('Хотя бы своё вернули!')
    
