'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
 А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
  Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
   который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
 Выполните вызов методов и также покажите результат.
'''

class Car:

    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return 'Старт'

    def stop(self):
        return 'Стоп'

    def turn(self, direction):
        return direction

    def show_speed(self):
        return self.speed

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости'
        return str(self.speed)

class SporCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости'
        return str(self.speed)

class PoliceCar(Car):
    pass


town_c = TownCar("Фиат", "Желтый", 69, False)
police_c = PoliceCar("Лада", "Белый", 98, True)
sport_c = SporCar("Ниссан", "Золотой", 122, False)
work_c = WorkCar("Газель", "Синий", 55, False)

print(town_c.__dict__)
print(police_c.__dict__)
print(sport_c.__dict__)
print(work_c.__dict__)

print(town_c.name, town_c.go(),  town_c.turn("прямо"), town_c.turn("Налево"), town_c.stop(), town_c.show_speed())
print(police_c.name, police_c.go(), police_c.turn("прямо"), police_c.turn("Направо"), police_c.stop(), police_c.show_speed())
print(sport_c.name, sport_c.go(), sport_c.turn("Направо"), sport_c.turn("Налево"), sport_c.stop(), sport_c.show_speed())
print(work_c.name, work_c.go(), work_c.turn("прямо"), work_c.turn("прямо"), work_c.stop(), work_c.show_speed())

