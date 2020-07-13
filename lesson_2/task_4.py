
user_string = input('Введите слова через пробел ')
for num, word in enumerate(user_string.split()):
    print(f'{num}: {word[:10]}')
