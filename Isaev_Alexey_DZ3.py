"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
использовать написанную ранее функцию int_func().
"""


# step 1
def int_func(word):
    return word[:1].upper() + word[1:].lower()


print(int_func('types'))


# step 2
def int_func(*word):
    for w in word:
        result = []
        for word in w.split():
            result.append(word[:1].upper() + word[1:].lower())
    return ' '.join(result)


print(int_func(
    'some types, such as ints, are able to use a more efficient algorithm when invoked using the three argument form.'))


# step 3
def ext_func(func, s):
    result = []
    for w in s.split():
        result.append(func(w))
    return ' '.join(result)


print(ext_func(int_func,
               'some types, such as ints, are able to use a more efficient algorithm when invoked using the three argument form.'))
