
# Реализовать функцию, принимающую несколько параметров, 
# описывающих данные пользователя: имя, фамилия, год рождения, 
# город проживания, email, телефон. Функция должна принимать 
# параметры как именованные аргументы. Реализовать вывод данных 
# о пользователе одной строкой.

def contacts(name, patname, birthday, city, email, phone):
    return f'{name} {patname} {bithday} {city} {email} {phone}'

name = 'John'
patname = 'Doe'
bithday = '1987'
city = 'London'
email = 'Doe@gmail.com'
phone = '+79991112233'

contacts(name=name, birthday=bithday, phone=phone, patname=patname, city=city, email=email)
