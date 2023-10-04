# Задание №3
# 📌 Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# 📌 Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой
# функции.

import json
import os

from typing import Callable
from functools import wraps

def main (func:Callable):
    dict_data:dict = {}
    @wraps(func)
    def wrapper(*args,**kwargs):
        nonlocal dict_data
        direct = 'Python\Practice\Lesson009'
        name_direct = 'Pra_less09_task3'
        full_direc = os.path.join(direct,name_direct)
        full_name = f'{full_direc}/{func.__name__}.json'
        try: # Создание новой директории если папка new_directory отсутствует
            os.mkdir(full_direc)
        except:
            pass
        data = func(*args,**kwargs)
        
        key = ','.join(list(map(str,args))+list((map(str,kwargs.items()))))

        if (f'{func.__name__}.json' not in os.listdir(full_direc)):
            dict_data[key] = [data]
        else:
            with open(full_name, 'r', encoding='utf-8') as f:
                dict_data = json.load(f)
                dict_data[key] = [data]                

       

        with open (full_name, 'w', encoding='UTF-8') as f_json:
            json.dump(dict_data,f_json,indent=2, separators=(',', ':'),ensure_ascii=False)


        return dict_data
    return wrapper

@main
def fibonacci (number:int, data: int):
    result = 0
    new_new_number = 0
    
    for i in range(2,number+1):
        new_number = result
        if (i == 2):
            result = 1
        else:
            result = new_number + new_new_number
            new_new_number = new_number

    return result 

