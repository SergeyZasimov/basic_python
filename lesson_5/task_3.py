# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

families = []
score = 0
my_file = open('Примеры_файлов/text_3.txt', 'r', encoding='utf-8')
for i, line in enumerate(my_file):
    line = line.split()
    family, salary = line[0], float(line[1])
    score += salary
    if salary < 20000:
        families.append(family)
my_file.close()
middle = score / (i + 1)

print('Сотрудники', families)
print('Средняя зарплата', middle)