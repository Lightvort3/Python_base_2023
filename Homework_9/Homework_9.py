#1. Создать класс TrafficLight (светофор).

print('Задача 1')
print()

from time import sleep

class TrafficLight:
    def __init__(self, colour):
        self.__colour = colour
    def swith(self):
        while True:   # - создаёт бесконечный цикл
            for key, value in self.__colour.items():
                sleep(value)
                print(key)

s = TrafficLight(colour = {
    'красный': 7,
    'жёлтый': 2,
    'зелёный': 1})

s.swith()

# 2. Реализовать класс Road (дорога).

print()
print('Задача 2')
print()

class Road:
    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self.square_meter_mass = thickness ** 2
        self.thickness = thickness
        self.mass = (length * width * 25 * 5)/1000
    def mass_method(self):
        print(f'Масса асфальта, необходимого для покрытия всей дороги составляет: ', self.mass, 'т')

mass_check = Road(20, 5000, 5)

mass_check.mass_method()

# 3. Реализовать базовый класс Worker (работник).

print()
print('Задача 3')
print()

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')
    def get_total_income(self):
        print(self._income["wage"] * self._income["bonus"])

p = Position('Petr', 'Ivanov', 'Developer', 100000, 1.3)

p.get_full_name(), p.get_total_income()

# 4. Реализуйте базовый класс Car.

print()
print('Задача 4')
print()

class Car:
    def __init__(self, speed, colour, name):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = bool
    def go(self, speed: float):
        try:
            self.speed = float(speed)
        except ValueError:
            pass
    def stop(self):
        self.speed = 0
    def turn_direction(self, direction: str):
        if direction not in ('right', 'left'):
            print(f'{direction} " - wrong direction"')
        if not self.speed:
            print('Speed up!')
        self.direction = direction
    def show_speed(self):
        print(f'Current speed is: ', self.speed, ' km/h')
        if (hasattr(self, 'max_speed')
            and self.speed > self.max_speed):
            print(f'Speed limit exceeded!')

class TownCar(Car):
    max_speed = 60

class SportCar(Car):
    pass

class WorkCar(Car):
    max_speed = 40

class PoliceCar(Car):
    def __init__(self, is_police):
        super().__init__(is_police)
        self.is_police = is_police

Work_example = WorkCar(68, 'Yellow', 'Samosval')
Work_example.show_speed()
Work_example.go(78)
Work_example.show_speed()
Work_example.go(37)
Work_example.show_speed()
Work_example.stop()
Work_example.show_speed()
Work_example.turn_direction('left')
Work_example.go(35)
Work_example.show_speed()
Work_example.turn_direction('lef')
Work_example.turn_direction('left')

# 5. Реализовать класс Stationery (канцелярская принадлежность).

print()
print('Задача 5')
print()

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def __init__(self):
        super().__init__(self)
        self.title = 'ручка'
    def draw(self):
        print(f'Надпись ручкой')

class Pencil(Stationery):
    def __init__(self):
        super().__init__(self)
        self.title = 'карандаш'
    def draw(self):
        print(f'Надпись карандашом')

class Handle(Stationery):
    def __init__(self):
        super().__init__(self)
        self.title = 'маркер'
    def draw(self):
        print(f'Выделение маркером')

p = Pen()
p.draw()

pp = Pencil()
pp.draw()

h = Handle()
h.draw()