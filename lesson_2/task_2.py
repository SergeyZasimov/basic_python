
print('Введите элементы списка. Для заверешения нажмите "q"')

basic_list = []
while True:
    element = input('Новый элемент ')
    if element == 'q':
        break
    basic_list.append(element)

print('Исходный список', basic_list)

for i in range(0, len(basic_list)-1, 2):
    basic_list[i], basic_list[i+1] = basic_list[i+1], basic_list[i]
print('Изменнёный список', basic_list)
