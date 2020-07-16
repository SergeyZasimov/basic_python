
# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, 
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, 
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. 
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
# Необходимо использовать написанную ранее функцию int_func().

def int_func(text):
    return text.capitalize()

def string_func(string):
    new_list = []
    for word in string.split():
        new_list.append(int_func(word))
    return ' '.join(new_list)

print(int_func('cat'))
print(string_func('cat dog'))
