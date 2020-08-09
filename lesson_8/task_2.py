class MyZeroDivisionError(Exception):
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return self.text

while True:
    inp = input('Введите выражение(q - выход) ')
    if inp == 'q': break
    else:
        try:
            if ('/' or '//' or '%') in inp and int(inp[-1]) == 0:
                raise MyZeroDivisionError('Деление на ноль запрещено!')
            else:
                print(eval(inp))
        except MyZeroDivisionError as err:
            print(err) 
        except NameError:
            continue