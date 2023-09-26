# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

import os
from task4 import generator_file

def generator_multi_file(directory: str,new_directory,list_dict:dict):
    """
    directory - директория в которой надо создать папку.
    new_directory - название папки, которую надо создать.

    """
    directory = f'{directory}/{new_directory}'
    try:
        os.mkdir(directory)
    except:
        pass

    for key in list_dict.keys():
        value = list_dict[key]

        generator_file(directory,f'file_{key}',extension=key,number_files=value)