'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

#Вариант через сравнение чисел

def my_func (var_1, var_2, var_3):
    if var_1 >= var_2 and var_2 >= var_3:
        summ = int(var_1 + var_2)
    elif var_1 >= var_2 and var_2 <= var_3:
        summ = int(var_1 + var_3)
    else:
        summ = int(var_3 + var_2)
    return summ


print(my_func(11, 13, 12))


# вариант через список и обраную сортировку

def my_func_1 (var_1, var_2, var_3):
    summ_list = [var_1, var_2, var_3]
    summ_list.sort(reverse=True)
    summ = int(summ_list[0] + summ_list[1])
    return summ


print(my_func_1(13, 16, 12))