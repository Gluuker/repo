'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
 А также класс «Оргтехника», который будет базовым для классов-наследников.
 Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
 В базовом классе определить параметры, общие для приведенных типов.
 В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
 передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
 а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
'''

class Storehouse:
    def __init__(self):
        self.list = {}

    def admission(self, officeequipment):
        self.list.setdefault(officeequipment.equpname(), []).append(officeequipment.modeltype())


class Officeequipment(Storehouse):
    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year
        self.group = self.__class__.__name__

    def equpname(self):
        return f'{self.group}'

    def modeltype(self):
        return f'{self.name} {self.price} {self.year}'


class Printer(Officeequipment):
    def __init__(self, name, price, color, year):
        super().__init__(name, price, year)
        self.color = color


class Scaner(Officeequipment):
    def __init__(self, name, price, year, network):
        super().__init__(name, price, year)
        self.network = network


class CopyMachine(Officeequipment):
    def __init__(self, name, price, year, portable):
        super().__init__(name, price, year)
        self.portable = portable


have = Storehouse()
while True:
    user_answ_choice = str(input('Если Вы хотите добавить технику введите "Add", если переместить "Move", выйти -"q" '))
    if user_answ_choice == "Add":
        while True:
            user_answ = str(input('Введите, что вы хотите добавить. Чтобы добавить Принтер введите "P", '
                  'чтобы добавить Сканер введите "S", чтобы добавить копировальную машину введите "C", чтобы прекратить'
                                  'ввод наберите "q" '))
            if user_answ == "P":
                device_1 = Printer(input("Name "), input("Price "), input("color "), input("year "))
                have.admission(device_1)
            else:
                if user_answ == "S":
                    device_1 = Scaner(input("Name "), input("Price "), input("year "), input("network "))
                    have.admission(device_1)
                else:
                    if user_answ == "C":
                        device_1 = CopyMachine(input("Name "), input("Price "), input("year "),input("portable "))
                        have.admission(device_1)
                    else:
                        if user_answ == "q":
                            break
                        else:
                            print("Некорректный ввод")
            print(f'Сейчас на складе: {have.list}')
    else:
        if user_answ_choice == "Move":
            print(f'Сейчас на складе: {have.list}') #для перемещения
        else:
            if user_answ_choice == "q":
                break
            else:
                print("Некорректный ввод")

