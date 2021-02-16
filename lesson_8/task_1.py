'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
 и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
  месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''
import time

user_date = time.strftime("%d-%m-%Y", time.localtime()) #ввод текущей даты в строке по заданному формату
#user_date = "42-11-2002" #данные для проверки числа
#user_date = "12-14-2002" #данные для проверки месяца
#user_date = "12-11-3" #данные для проверки года


class Data:
    def __init__(self, user_date):
        self. user_date = str(user_date)

    @classmethod
    def digit(cls, user_date):
        return Data.check(user_date)

    @staticmethod
    def check(user_date):
        day, month, year = map(int, user_date.split('-'))
        if day !=0 and day <= 31:
            if month !=0 and month <= 12:
                if year > 2000:
                    return day, month, year
                else:
                    return "Год не может быть меньше 2000"
            else:
                return "Введите месяц от 1 до 12"
        else:
            return "Введите дату от 1 до 31"



date = Data.digit(user_date)
print(date)
