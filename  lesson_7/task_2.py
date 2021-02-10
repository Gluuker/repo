'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
 Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
  К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
   размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod

class Garb (ABC):
    def __init__(self, argument):
        self.argument = argument
    @property
    def expenses(self):
        return f'Сумма затраченной ткани равна: {self.argument / 6.5 + 0.5 + 2 * self.argument + 0.3 :.2f}'

    @abstractmethod
    def param(self):
        pass

class Greatcoat(Garb):
    def expenses(self):
        return f'Пальто: {self.argument / 6.5 + 0.5 :.2f} единиц'
    def param(self):
        pass

class Suit(Garb):
    def expenses(self):
        return f'Костюм: {2 * self.argument  + 0.3 :.2f} единиц'
    def param(self):
        pass

cloth_1 = Greatcoat(54)
cloth_2 = Suit(174)
print(cloth_1.expenses())
print(cloth_2.expenses())
