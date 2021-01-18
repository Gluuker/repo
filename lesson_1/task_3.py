max_numb = 0

while True:
    user_numb = input("Введите целое положительное число:")
    try:
        user_numb = int(user_numb)

        while user_numb > 0:
            b = user_numb % 10
            user_numb = user_numb // 10

            if b > max_numb:
                max_numb = b


    except ValueError:
        print('Введите положительное числовое значение!')
    else:
        print(f'Самое большая цифра: {max_numb}')
        break
