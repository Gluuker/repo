'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

В данном случае, файл file_task_4.txt исходник,
а файлы file_task_4_new.txt и file_task_4_new2.txt результат для первого и второго варианта соответственно.
'''
# 1 вариант, выглядит, с моей точки зрения как "костыль"
with open("file_task_4.txt", "r", encoding="utf-8") as file:
    file_list = file.readlines()
    for line in file_list:
        line = line.replace("\n", "")
        line = line.replace("One", "Один")
        line = line.replace("Two", "Два")
        line = line.replace("Three", "Три")
        line = line.replace("Four", "Четыре")
        with open("file_task_4_new.txt", "a", encoding="utf-8") as file_new:
            print(line, file=file_new)
# 2 вариант,  через словарь
transl_dict = {"One": 'Один', "Two": 'Два', "Three": 'Три', "Four": 'Четыре'}
with open("file_task_4.txt", "r", encoding="utf-8") as file:
    file_list = file.readlines()
    for line in file_list:
        line = line.replace("\n", "")
        line_list = line.split()
        line_list[0] = transl_dict.get(line_list[0])

        with open("file_task_4_new2.txt", "a", encoding="utf-8") as file_new_2:
            print(" ".join(line_list), file=file_new_2)
