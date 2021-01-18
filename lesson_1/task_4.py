
while True:
    revenue = input("Введите Вашу выручку:")
    cost = input("Введите Ваши издержки:")
    try:
        revenue = int(revenue)
        cost = int(cost)
        if revenue < cost:
            print("Вы работатете в убыток!")
        else:
            print("Вы работаете в прибыль!")
            cost_effect = ((revenue - cost) / revenue) * 100
            print(f'Ваша рентабельность состваляет {cost_effect:.2f}%')
            while True:
                staff = input("Введите количество сотрудников:")
                try:
                    staff = int(staff)
                    cost_effect_staff = (revenue - cost) / staff
                    print(f'Прибыль фирмы на одного сотрудника составляет {cost_effect_staff:.2f}')
                except ValueError:
                    print('Введите положительное числовое значение!')
                else:
                    break

    except ValueError:
        print('Введите положительное числовое значение!')
    else:
        break