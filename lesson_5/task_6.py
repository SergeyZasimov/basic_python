# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
# словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re
lessons = {}
myRegex = re.compile(r'([a-zA-Z]+): (\d+)?-?\(?\w*\)? (\d+)?-?\(?\w*\)? (\d+)?-?\(?\w*\)?')
with open('Примеры_файлов/text_6.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        res = myRegex.search(line)
        lesson = res.groups()
        time = [int(num) for num in lesson[1:] if num]
        lessons[f"{lesson[0]}"] = sum(time)
print(lessons)