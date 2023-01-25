# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен

print('Задача 1')
print()

import re

re_email = re.compile(r'(?P<username>[a-zA-Z0-9.\-_]+)@(?P<domain>[a-zA-Z0-9.\-_]+)')

def email_parse(email):
    try:
        is_valid = map(lambda x: x.groupdict(), re_email.finditer(email))
        print(is_valid.__next__())
    except:
        raise ValueError(f'wrong email: {email}') from ValueError


enter_email = email_parse(input('Введите адрес электронной почты (не завбывайте про разделители "@" и "." ): '))

print(enter_email)

# 3. Написать декоратор для логирования типов позиционных аргументов функции

print()
print('Задача 3')
print()

from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*argv):
        return 'calc_cube({0})'.format(", ".join([f"{func(c)}:{type(func(c))}" for c in argv]))
    return wrapper

@type_logger
def calc_cube(c):
    return c ** 3

a = calc_cube(5)
print(a)

# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции

print()
print('Задача 4')
print()

def val_checker(lambda_set):
    def try_exception(func):
        @wraps(func)
        def wrapper(x):
            if lambda_set(x):
                return func(x)
            raise ValueError(f'wrong val: {x}') from ValueError
        return wrapper
    return try_exception

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

b = calc_cube(-5)
print(b)

f = calc_cube(5)
print(f)