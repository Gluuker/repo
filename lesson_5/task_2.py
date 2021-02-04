'''
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

'''В данной задаче столкнулся с проблемой, решение которых не смог найти:
1) Если открываем файл и выводим исходный, то при попытке после первого print сделать:
    file_list = file.readlines()
    sum_line = len(file_list)
    итог расчета 0. 
    
    По результату дважды открывал файл
'''

with open("file_task_2.txt", "r", encoding="utf-8") as file:
    txt = file.read()
    print(f"Исходный файл:\n{txt}")

with open("file_task_2.txt", "r", encoding="utf-8") as file:
    file_list = file.readlines()
    sum_line = len(file_list)
    print(f"\nКоличество строк в файле: {sum_line}")
    for line in file_list:
        line = line.replace("\n", "")
        word_line = line.split()
        sum_word_line = len(word_line)
        print(f'Количество слов в строке "{line}": {sum_word_line}')
