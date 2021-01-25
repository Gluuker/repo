'''
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

# вариант с запросом длины списка
print("Вариант решения 1: Запрашиваем у пользователя длину списка")
list_numb = int(0)
my_list = []
new_list = []

while True:
    try:
        quantity_user = int(input("Введите длину списка "))
        while list_numb < quantity_user:
            el_list = input(f"Введите {list_numb + 1} элемент списка ")
            my_list.append(el_list)
            list_numb += 1
        else:
            print("Ваш список: ", my_list)
            list_numb = int(0) # Переменная используется как счетчик, обнулил ее для нового расчета
            first_num_el = int(0)
            if (quantity_user % 2) == 0:
                while list_numb < (quantity_user // 2):
                    second_num_el = int(first_num_el + 1)
                    new_list.append(my_list[second_num_el])
                    new_list.append(my_list[first_num_el])
                    first_num_el += 2
                    list_numb += 1
                else:
                    print("Новый список: ", new_list)
            else:
                while list_numb < (quantity_user // 2):
                    second_num_el = int(first_num_el + 1)
                    new_list.append(my_list[second_num_el])
                    new_list.append(my_list[first_num_el])
                    first_num_el += 2
                    list_numb += 1
                else:
                    new_list.append(my_list[quantity_user - 1])
                    print("Новый список: ", new_list)
    except ValueError:
        print('Введите положительное числовое значение!')
    else:
        break

# Вариант с вводом пустой строки для остановки
print("\n\nВариант решения 2: Остановка по пустому элементу")
print('Для остановки заполнения, при запросе, нажмите "Enter"')
list_numb = int(0)
my_list = []
new_list = []
el_list = int()
while True:
    try:
        while el_list != "":
            el_list = input(f"Введите {list_numb + 1} элемент списка ")
            my_list.append(el_list)
            list_numb += 1
        else:
            my_list.pop(list_numb-1)
            print("Ваш список: ", my_list)
            list_numb = int(0) # Переменная используется как счетчик, обнулил ее для нового расчета
            first_num_el = int(0)
            if ((len(my_list)) % 2) == 0:
                while list_numb < ((len(my_list)) // 2):
                    second_num_el = int(first_num_el + 1)
                    new_list.append(my_list[second_num_el])
                    new_list.append(my_list[first_num_el])
                    first_num_el += 2
                    list_numb += 1
                else:
                    print("Новый список: ", new_list)
            else:
                while list_numb < ((len(my_list)) // 2):
                    second_num_el = int(first_num_el + 1)
                    new_list.append(my_list[second_num_el])
                    new_list.append(my_list[first_num_el])
                    first_num_el += 2
                    list_numb += 1
                else:
                    new_list.append(my_list[(len(my_list)) - 1])
                    print("Новый список: ", new_list)
    except ValueError:
        print('Введите положительное числовое значение!')
    else:
        break