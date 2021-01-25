'''
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''
def int_func (elem_list):
    return elem_list.title()

user_world = input("Введите свое предложение ")
user_world.split(" ")
user_world_list = user_world.split(" ")
user_world_list_new = list()

for elem_list in user_world_list:
    user_world_list_new.append(int_func(elem_list))

print(' '.join(user_world_list_new))