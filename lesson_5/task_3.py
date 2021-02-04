'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''

with open("file_task_3.txt", "r", encoding="utf-8") as file:
    txt = file.read()
    print(f"Исходный файл:\n{txt}")

with open("file_task_3.txt", "r", encoding="utf-8") as file:
    file_list = file.readlines()
    print("\nСписок сотрудников с окладом менее 20 тыс:")
    sum_cash = int(0)
    for line in file_list:
        line = line.replace("\n", "")
        employee = line.split()
        i = int(employee[1])
        sum_cash = sum_cash + i
        if i < 20000:
            print(employee[0])
    mid_income = sum_cash / len(file_list)
    print(f'Средняя величина дохода всех сотрудников {mid_income}')