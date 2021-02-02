'''
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
 Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
'''

from itertools import count
from itertools import cycle
# а)
start_number = None

while start_number is None:
    try:
        start_number = int(input('Введите начальное число: '))
    except ValueError:
        print('Введите корректное значение')
stop_step = int(input('Введите максимальное число: '))
for number in count(start_number):
    print(number)
    if number == stop_step:
        break

# б)
max_dubl = int(input('Введите максимальное число повторов: '))
stop_step = 0

new_list = ['Прямо', 'Налево', 'Направо']
for el in cycle(new_list):
    print(el)
    stop_step += 1
    if stop_step > max_dubl - 1:
        break