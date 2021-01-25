'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict
'''
# Решение через list
print("Решение через list")
name_month = ['Зима', 'Весна', 'Лето', 'Осень']
while True:
    try:
        user_month = int(input("Введите номер месяца "))
        if user_month <= 12 and user_month > 0:
            if user_month == 1 or user_month == 2 or user_month == 12:
                print("Время года ", name_month[0])
            elif 2 < user_month <= 5:
                print("Время года ", name_month[1])
            elif 5 < user_month <= 8:
                print("Время года ", name_month[2])
            elif 8 < user_month <= 11:
                print("Время года ", name_month[3])
        else:
            print("Введите значение от 1 до 12")
            continue

    except ValueError:
        print('Введите положительное числовое значение от 1 до 12!')

    else:
        break

# Решение через dict
print("\nРешение через dict")
name_month = {1 :"Зима", 2 :"Зима", 3 :"Весна", 4 :"Весна", 5 :"Весна", 6 : "Лето", 7 : "Лето", 8 : "Лето", 9 : "Осень", 10 : "Осень", 11 : "Осень", 12 :"Зима"}
while True:
    try:
        user_month = int(input("Введите номер месяца "))
        if user_month <= 12 and user_month > 0:
            print(name_month.get(user_month))
        else:
            print("Введите значение от 1 до 12")
            continue

    except ValueError:
        print('Введите положительное числовое значение от 1 до 12!')

    else:
        break
