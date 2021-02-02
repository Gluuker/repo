"""
2. Представлен список чисел.
 Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
"""
from random import randint

first_list = [randint(0, 100) for i in range(10)]
print(f"Изначальный список {first_list}")
second_list = []
i = int(0)
for max_numb in first_list:
    if max_numb >= i:
        second_list.append(max_numb)
        i = int(max_numb)
    i = int(max_numb)

print(f"Итоговый список {second_list}")