class MyValidException(Exception):
    def __str__(self):
        return 'Текст не будет добавлен в список!'

def validator(inp):
    if not inp.isdigit():
        raise MyValidException

myList = []
while True:
    try:
        inp = input('Введите число (q - выход) ') 
        if inp == 'q': break
        else:
            validator(inp)
            myList.append(int(inp))
    except MyValidException as err:
        print(err)
print(myList)