'''
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

from functools import reduce


def multiplier(numb_1, numb_2):
    return numb_1 * numb_2


new_list = [i for i in range(100, 1001) if i % 2 == 0]
print(f"исходный список {new_list}")
result = reduce(multiplier, new_list)
print(f"произведение  {result}")
