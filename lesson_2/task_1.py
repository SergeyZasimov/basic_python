
my_list = [10, 25.3, 'tower', ['cat', 'dog'], {'food':'apple', 'num': 1}, (3, 4), None, b'android', 
           bytearray(b'hello'), True]
for element in my_list:
    print(f'{str(element):<30} => {type(element)}')
