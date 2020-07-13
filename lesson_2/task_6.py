print('Товары')
goods = []
for i in range(1, 4):
    print('Новый товар')
    info = {}
    info['название'] = input('Введите название товара ')
    info['цена'] = int(input('Введите цену товара '))
    info['количество'] = int(input('Введите количество товара '))
    info['ед'] = input('Введите единицу измерения ')
    goods.append((i, info))
print(goods)

# goods = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}), 
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
# ]


analis = {
    'название': [],
    'цена': [],
    'количество': [],
    'eд': []
}

for good in goods:
    for key in good[1]:
        if good[1][key] not in analis[key]:
            analis[key].append(good[1][key])
for key in analis:
        print(f'{key}: {analis[key]}')
