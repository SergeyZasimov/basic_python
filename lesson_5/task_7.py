# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json
firms = {}
with open('Примеры_файлов/text_7.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        name, form, revenue, charge = line.split()
        firms[name] = int(revenue) - int(charge)
profits = []
i = 0
for profit in firms.values():
    if profit > 0:
        profits.append(profit)
        i += 1
average_profit = {'average_profit': (sum(profits))/i}

result = [firms, average_profit]

with open('Примеры_файлов/text_7my_json.json', 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file, ensure_ascii=False, indent=4)
