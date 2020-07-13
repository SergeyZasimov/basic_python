
seasons = {
              'весна':['март', 'апрель', 'май'], 
              'лето': ['июнь', 'июль', 'август'],
              'осень':['сентябрь', 'октябрь', 'ноябрь'],
              'зима': ['декабрь', 'январь', 'февраль']
}

months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 
          'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

user_month = input('Введите номер месяца [1-12] ')
while (not user_month.isdigit()) or (int(user_month) not in range(1, 13)):
    user_month = input('Введите номер месяца [1-12] ')
    
month = months[int(user_month) - 1]
print('Месяц:', month)

for season in seasons:
    if month in seasons[season]:
        print('Время года:', season)
