import os
from pathlib import Path

dir_list = os.listdir()
for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end='\t') # Определяет, является объект папкой
    print(f'{os.path.isfile(obj) = }', end='\t') # Определяет, является объект файлом
    print(f'{os.path.islink(obj) = }', end='\t') # Определяет, является объект ссылкой
    print(f'{obj = }') # Выводит название объекта

p = Path(Path().cwd())
for obj in p.iterdir():
    print(f'{obj.is_dir() = }', end='\t') # Определяет, является объект папкой
    print(f'{obj.is_file() = }', end='\t') # Определяет, является объект файлом
    print(f'{obj.is_symlink() = }', end='\t') # Определяет, является объект ссылкой
    print(f'{obj = }') # Выводит полный путь к объекту