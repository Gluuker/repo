'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
 а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
 а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
import json

f_dict = {}
s_dict = {}
result_list = []

sum_profit = int(0)
with open("file_task_7.txt", "r", encoding="utf-8") as file:
    file_list = file.readlines()
    sum_comp = len(file_list)
    for line in file_list:
        line = line.replace("\n", "")
        line_list = line.split()
        numb_line_list = [int(a) for a in line_list[2::]]
        profit = numb_line_list[0]- numb_line_list[1]
        f_dict[line_list[0]] = profit
        if profit >= 0:
            sum_profit = sum_profit + profit
        else:
            sum_comp = sum_comp - 1

    s_dict["sum_profit"] = sum_profit / sum_comp
    result_list.append(f_dict)
    result_list.append(s_dict)

    result_list

with open("task_7.json", "w") as write_f:
    json.dump(result_list, write_f)
