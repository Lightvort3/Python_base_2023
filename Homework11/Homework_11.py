# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».

print('Задача 1', '\n')

from datetime import date


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def int_extractor(cls, date):
        day, month, year = [int(d) for d in date.split('-')]
        return f'{type(day), day}\n{type(month), month}\n{type(year), year}'

    @staticmethod
    def int_validator(date):
        try:
            day, month, year = [int(d) for d in date.split('-')]
        except ValueError:
            return 'Валидация даты не пройдена'
        if not 1 <= day <= 31:
            return 'Валидация даты не пройдена по дню'
        if month in [4, 6, 9, 11] and day == 31:
            return 'Валидация даты не пройдена по сочетанию дня и месяца'
        if month == 2 and day in [29, 30, 31]:
            return 'Валидация даты не пройдена по сочетанию дня и месяца'
        if not 1 <= month <= 12:
            return 'Валидация даты не пройдена по месяцу'
        if not year > 0:
            return 'Валидация даты не пройдена по году'
        return 'Валидация даты пройдена'


print(Date.int_extractor('19-08-1985'))
print(Date.int_validator('19-08-1985'))
print(Date.int_validator('19081985'))
print(Date.int_validator('119-08-1985'))
print(Date.int_validator('31-09-1985'))
print(Date.int_validator('29-02-1985'))
print(Date.int_validator('19-18-1985'))
print(Date.int_validator('19-08-0'))

# 2.  Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.

print('\n', 'Задача 2', '\n')


class Stopnull(Exception):
    def __init__(self, warning):
        self.warning = warning


def null_check():
    try:
        divisible = int(input('Делимое: '))
        divider = int(input('Делитель: '))
        if divider == 0:
            raise Stopnull('Делить на ноль может только Чак Норрис!')
        else:
            division = divisible / divider
            return division
    except Stopnull as no_break:
        return no_break


print(null_check())

# 3.  Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.

print('\n', 'Задача 3', '\n')


class Intdefender(Exception):
    def __init__(self):
        pass


class Intcheck:
    def __init__(self):
        self.infinite_list = []

    def input_check(self):
        global some_input
        while True:
            try:
                try:
                    some_input = int(input('Число для списка: '))
                    proceed = input(f'Чтобы остановиться, введите команду "stop". Чтобы продолжить, нажмите Enter: ')
                    self.infinite_list.append(some_input)
                    if proceed == 'stop':
                        print(self.infinite_list)
                        break
                except ValueError:
                    raise Intdefender
            except Intdefender:
                proceed = input(
                    f'На ввод принимаются только числа!' '\n' 'Чтобы остановиться, введите команду "stop". Чтобы продолжить, нажмите Enter: ')
                if proceed == 'stop':
                    print(self.infinite_list)
                    break
                else:
                    pass


i = Intcheck()
i.input_check()

# 4.-6. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Реализуйте механизм валидации вводимых пользователем данных.

print('\n', 'Задачи 4-6', '\n')


class Store_description:
    def __init__(self, store_name, store_adress, store_square, store_units):
        self.store_name = store_name
        self.store_adress = store_adress
        self.store_square = float(store_square)
        self.store_units = int(store_units)


class Office_equipment:
    def __init__(self, item_name, item_price, item_quantity, item_cell_size=('large', 'medium', 'small')):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_cell_size = item_cell_size
        self.items_summ_price = float(item_price * item_quantity)
        self.items = {'Наименование позиции': self.item_name, 'Цена за 1 шт.': self.item_price, 'Количество товара': self.item_quantity, 'Размер хранения': self.item_cell_size, 'Общая стоимость': self.items_summ_price}
    def item_registration(self):
        try:
            item_name = input(f'Наименование товара: ')
            item_price = float(input(f'Цена товара за 1 шт.: '))
            item_quantity = int(input(f'Количество товара в шт.: '))
            item_cell_size = self.item_cell_size
            items_summ_price = float(item_price * item_quantity)
            item_position = {'Наименование позиции': item_name, 'Цена за 1 шт.': item_price, 'Количество товара': item_quantity, 'Размер хранения': item_cell_size, 'Общая стоимость': items_summ_price}
            self.items.update(item_position)
            print(self.items)
        except ValueError:
            print('Ошибка ввода!')

class Printer(Office_equipment):
    def __init__(self, item_name, item_price, item_quantity):
        super().__init__(item_name, item_price, item_quantity, item_cell_size='medium')

class Scanner(Office_equipment):
    def __init__(self, item_name, item_price, item_quantity):
        super().__init__(item_name, item_price, item_quantity, item_cell_size='small')

class Copier(Office_equipment):
    def __init__(self, item_name, item_price, item_quantity):
        super().__init__(item_name, item_price, item_quantity, item_cell_size='large')

printer = Printer('Canon', 10500.5, 25)
scanner = Scanner('HP', 5000.2, 30)
copier = Copier('Xerox', 25000.0, 5)

printer.item_registration()
scanner.item_registration()
copier.item_registration()

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».

print('\n', 'Задача 7', '\n')

class Complex_num:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
    def __add__(self, other):
        return f'Результат сложения: {self.num_1 + other.num_1} + {self.num_2 + other.num_2}'
    def __mul__(self, other):
        return f'Результат умножения: {self.num_1 * other.num_1 - (self.num_2 * other.num_2)} + {self.num_2 + other.num_1}'

compl_1 = Complex_num(500, -1500)
compl_2 = Complex_num(400, 1200)

print(compl_1 + compl_2)
print(compl_1 * compl_2)