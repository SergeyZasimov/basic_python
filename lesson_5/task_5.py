# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('Примеры_файлов/text_5.txt', 'w+', encoding='utf-8') as my_file:
    text = input('Введите набор чисел, разделенных пробелами ')
    my_file.write(text)
    my_file.seek(0)
    line = my_file.readline()
    result = sum(map(int, line.split()))
print(result)