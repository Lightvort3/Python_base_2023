# 1. Реализовать класс Matrix (матрица).

print('Задача 1', '\n')

from typing import List


class Matrix:
    def __init__(self, list_of_lists: List[List]):
        self.matrix = list_of_lists
        rows = len(self.matrix)
        self.__matrix_size = set([(rows, len(row)) for row in self.matrix])

    def __add__(self, other: "Matrix") -> "Matrix":
        mtrx_summ = []
        for item in zip(self.matrix, other.matrix):
            mtrx_summ.append([sum([m, n]) for m, n in zip(*item)])
        return Matrix(mtrx_summ)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])


mtrx_first = Matrix([[31, 22], [37, 43], [51, 86], [3, 5, 32]])
print('First matrix:', '\n', mtrx_first, '\n')
mtrx_scnd = Matrix([[2, 4, 6], [-1, 64, -8], [3, 5, 8, 3], [8, 3, 7, 1]])
print('Second matrix:', '\n', mtrx_scnd, '\n')

print('United matrix:', '\n', mtrx_first + mtrx_scnd)

# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. .

print('\n', 'Задача 2', '\n')

class Clothes:
    def __init__(self, V, H):
        self.V = V
        self.H = H
        self.expense_1 = self.V / 6.5 + 0.5
        self.expense_2 = 2 * self.H + 0.3
    @property
    def cnsmptn(self):
        return f'Общий подсчёт расхода ткани: {self.expense_1 + self.expense_2}'


class Coat:
    def __init__(self, V):
        self.V = V
    def cnsmptn(self):
        return f'Расход ткани для пальто: {self.V / 6.5 + 0.5}'


class Costume:
    def __init__(self, H):
        self.H = H
    def cnsmptn(self):
        return f'Расход ткани для костюма: {2 * self.H + 0.3}'

coat = Coat(1950)
costume = Costume(50)
whole = Clothes(1950, 50)
print(coat.cnsmptn())
print(costume.cnsmptn())
print(whole.cnsmptn)

# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек.

print('\n', 'Задача 3', '\n')

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
    def __add__(self, other):
        return f'Результат сложения клеток: {self.quantity + other.quantity}'
    def __sub__(self, other):
        sub_res = self.quantity - other.quantity
        return f'Результат вычитания: {sub_res}' if sub_res > 0 else f'Ошибка! Разность количества ячеек двух клеток должна быть больше нуля'
    def __mul__(self, other):
        return f'Результат умножения клеток: {self.quantity * other.quantity}'
    def __floordiv__(self, other):
        return f'Результат деления клеток: {self.quantity // other.quantity}'
    def make_order(self, rows):
        order_res = ''
        for c in range(int(self.quantity / rows)):
            order_res += '*' * rows + '\n'
        order_res += '*' * (self.quantity % rows) + '\n'
        return order_res

cell_first = Cell(35)
cell_second = Cell(5)

print(cell_first + cell_second)
print(cell_first - cell_second)
print(cell_first * cell_second)
print(cell_first // cell_second)
print(cell_first.make_order(5))