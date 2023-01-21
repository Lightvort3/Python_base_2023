# 1. Написать скрипт, создающий стартер (заготовку) для проекта со структурой папок

print('Задача 1')
print()
import os

#dir_path = os.path.join('my_project', 'settings', 'mainapp', 'adminapp', 'authapp') - создаёт папки, вложенные друг в друга

structure = {'my_project': [{'settings': [], 'mainapp': [], 'adminapp': [], 'authapp': []}]}

def starter(parent, nest):
    for p, n in nest.items():
        dir_path = os.path.join(parent, p)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        if len(n) > 0:
            for folder in n:
                starter(dir_path, folder)

if __name__ == '__main__':
    starter(os.getcwd(), nest=structure)

# 3. Написать скрипт, который собирает все шаблоны в одну папку templates

print()
print('Задача 3')
print()

import shutil

root_path = r'C:\Users\Иванищевы\Documents\GeekBrains\BI-аналитика\Python_base_2023\Homework7\my_project'
files = [os.path.relpath(os.path.join(root, file), root_path)
              for root, _, files in os.walk(root_path)
              for file in files if file.endswith('.html')]
for check_path in files:
    path, file = os.path.split(check_path)
    new_path = os.path.join(root_path, 'templates', path)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    shutil.copyfile(os.path.join(root_path, check_path), os.path.join(new_path, file))

# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря

print()
print('Задача 4')
print()

from collections import defaultdict
from os.path import relpath
import django

django_files = {}
root_dir = r'C:\Users\Иванищевы\Documents\GeekBrains\BI-аналитика\Python_base_2023\Homework7\some_data'

for root, dirs, files in os.walk(root_dir):
    for file in files:
        ext = os.path.join(root, file)
        bit = 10 ** (len(str(os.stat(ext).st_size)) - 1)
        rel_path = relpath(os.path.join(root, file), root_dir)
        if bit not in django_files:
            django_files[bit] = django_files.get(bit, 0) + 1

for bit, files in sorted(django_files.items(),
                         key=lambda x: x[1], reverse=True):
    print(f'{bit}: {files}')