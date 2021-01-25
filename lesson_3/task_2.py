'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой
'''
def output_info (name, sec_name, year, city, mail, tel):
    print(name, sec_name, year, city, mail, tel)



user_name = input("Введите Ваше имя: ")
user_sec_name = input("Введите Вашу фамилию: ")
user_year_b = input("Введите год рождения: ")
user_city = input("Введите Ваш город: ")
user_email = input("Введите Вашу почту: ")
user_tel_num = input("Введите Ваш номер телефона: ")

output_info(name = user_name, sec_name = user_sec_name, year = user_year_b, city = user_city, mail = user_email, tel = user_tel_num)


