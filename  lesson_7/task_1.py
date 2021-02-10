'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
 (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
 матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:
    def __init__(self, first_list):
        self.first_list = first_list

    def __str__(self):
        for k in self.first_list:
            for i in k:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.first_list)):
            for n in range(len(other.first_list[i])):
                self.first_list[i][n] = self.first_list[i][n] + other.first_list[i][n]
        return Matrix.__str__(self)

first_matrix = Matrix (
    [
        [1,1,1],
        [2,2,2],
        [3,3,3]
    ]
)
second_matrix = Matrix(
    [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]
)
print(first_matrix.__str__())
print(second_matrix.__str__())
print(first_matrix.__add__(second_matrix))
