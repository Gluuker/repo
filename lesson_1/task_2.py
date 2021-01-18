while True:

    user_numb = input("Введите положительное число:")

    try:
        double_numb = int(user_numb * 2)
        triple_numb = int(user_numb * 3)
        user_numb = int(user_numb)
        sum_numb = int(user_numb + double_numb + triple_numb)

    except ValueError:
        print('Введите положительное числовое значение!')
    else:
        print(f'Сумма чисел по формуле n+nn+nnn={user_numb}+{double_numb}+{triple_numb}={sum_numb}')
        break
