'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
from random import randint
numb_list = []
numb_result =[]
with open("file_task_5.txt", "w", encoding="utf-8") as file:
    i = int(0)
    while i < 10:
        numb_list.append(str(randint(0, 10)))
        i += 1
    print(" ".join(numb_list), file=file)

with open("file_task_5.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

with open("file_task_5.txt", "r", encoding="utf-8") as file:
    file_list = file.readlines()
    for line in file_list:
        line = line.replace("\n", "")
        numb_list_line = line.split()
    numb_result = [int(a) for a in numb_list_line]
    print(f'Сумма значений равно {sum(numb_result)}')
