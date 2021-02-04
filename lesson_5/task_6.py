'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
ed_dict = {}
with open("file_task_6.txt", "r", encoding="utf-8") as file:
    file_list = file.readlines()
    for line in file_list:
        line = line.replace("\n", "")
        line = line.replace(":", "")
        line = line.replace("—", "")
        line = line.replace("(л)", "")
        line = line.replace("(пр)", "")
        line = line.replace("(лаб)", "")
        line = line.replace(".", "")
        line_list = line.split()
        numb_line_list = [int(a) for a in line_list[1::]]
        ed_dict[line_list[0]] = sum(numb_line_list)

    print(ed_dict)