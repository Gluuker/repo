'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
def split_num (user_answ_frst, user_answ_sec):
    f_s = user_answ_frst / user_answ_sec
    s_f = user_answ_sec / user_answ_frst
    print(f'Деление первого числа на второе: {f_s:.2f}')
    print(f'Деление второго числа на первое: {s_f:.2f}')

while True:
    try:
        user_answ_frst = int(input ("Введите первое число "))
        user_answ_sec = int(input ("Введите второе число "))
        while user_answ_frst != 0 and user_answ_sec != 0:
            split_num (user_answ_frst, user_answ_sec)
            break

        else:
            print("Деление на 0 в данной задаче не возможно")
            continue
    except ValueError:
        print('Введите числовое значение!')
    else:
        break