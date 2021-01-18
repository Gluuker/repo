while True:

    first_day = input("Сколько пробежал спортсмен в первый день? ")
    max_dist = input("Для какого макисмального результата определить день? ")

    try:
        first_day = int(first_day)
        max_dist = int(max_dist)
        dist = first_day
        day = 1
        while dist < max_dist:
            dist = dist + (dist * 0.1)
            day += 1
           # print(f'{day} {dist}') для проверки правильности рассчета




    except ValueError:
        print('Введите положительное числовое значение!')
    else:
        print(f'На {day}-й день спортсмен достиг результата - не менее {max_dist} км')
        break