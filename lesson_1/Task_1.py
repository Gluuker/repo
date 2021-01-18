while True:

    user_time = input("Введите время в секундах:")

    try:
        user_time = int(user_time)
        hr_time = user_time // 3600
        min_time = (user_time // 60) - (hr_time * 60)
        sec_time = user_time - (hr_time * 3600) - (min_time * 60)

    except ValueError:
        print('Введите положительное числовое значение!')
    else:
        if hr_time < 10:
            print(f"Введенное значение в формате чч:мм:сс : {hr_time:02}:{min_time:02}:{sec_time:02}")

        else:
            print(f'Введенное значение в формате чч:мм:сс : {hr_time}:{min_time:02}:{sec_time:02}')
        break
