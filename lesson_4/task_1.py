
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. 
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys

def work_pay(hours, rate, prize):
    return f'Заработная плата = {(hours * rate) + prize}'

hours, rate, prize = sys.argv[1:]
if hours.isalpha() or rate.isalpha() or prize.isalpha():
    print('В следующий раз введите числа!')
else:
    print(work_pay(int(hours), int(rate), int(prize)))
