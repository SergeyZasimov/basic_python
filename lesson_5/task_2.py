# Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

result = {}
my_file = open('Примеры_файлов/text_1.txt', 'r', encoding='utf-8')
for i, line in enumerate(my_file):
    result[i + 1] = len(line.split())
my_file.close()
print(result)