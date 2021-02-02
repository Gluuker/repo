"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
  Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

def calcpay(hours, rate, bonus):
    try:
        return int(hours) * int(rate) + int(bonus)
    except ValueError:
        print('Введите корректные значения')
        return 0

dir_1, name, hours, rate, bonus = argv

pay = calcpay(hours, rate, bonus)
print(f'Сотрудник {name} должен получить {pay} рублей')