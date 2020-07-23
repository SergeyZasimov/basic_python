# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные
# должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл

dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('Примеры_файлов/text_4.txt', 'r', encoding='utf-8') as my_file:
    with open('Примеры_файлов/text_4n.txt', 'w', encoding='utf-8') as new_file:
        for line in my_file:
            word, sign, num = line.split()
            print(f'{dict[word]} {sign} {num}', file=new_file)
