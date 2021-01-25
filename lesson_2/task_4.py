'''
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
'''
i = int(0)
user_world = input("Введите свое предложение ")
user_world.split(" ")
user_world_list = user_world.split(" ")
print(user_world_list)
print(len(user_world_list))
for tmp in user_world_list:
   print(i + 1, tmp[0:10])
   i += 1
