# Задание №2
# 📌 Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в
# JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
import os

def input_number_min_max (*,number_min:int = 0,number_max:int = 100,text:str):
    """
    Функция ввода чисел от number_min до number_max.
    """
    
    while True:
        try:
            number = int(input (text))
            if (number < number_min):
                print(f'Число введено меньше {number_min}, введите число заново.')
                continue
            elif (number > number_max):
                print(f'Число введено больше {number_min}, введите число заново.')
                continue
            else:
                break
        except:
            print(f'Введённое значение не являются числом!!!. Введите число заново.')
            continue
    return number

def input_number_min (*,number_min:int = 0,text:str):
    """
    Функция ввода чисел от number_min до number_max.
    """
    
    while True:
        try:
            number = int(input (text))
            if (number < number_min):
                print(f'Число введено меньше {number_min}, введите число заново.')
                continue
            else:
                break
        except:
            print(f'Введённое значение не являются числом!!!. Введите число заново.')
            continue
    return number

def personal_data_json(directory:str, new_directory:str,*,name_file_json:str):
    """
    Функция считывает json файл и изымает из него данные. Потом принимает данные в ведённые с консоли
    Имя, ID - уникальные, проверяется, уровень доступа(1,7). Все данные после выхода
    из меню записывает в json файл.

    directory:str - путь до директории где создаётся новая папка new_directory
     name_file_json:str - имя файла json без расширения json
    """

    full_direc = f'{directory}/{new_directory}' #Директория  с новой папкой
    file_jsone = f'{name_file_json}.json'
    full_name_file_json = f'{full_direc}/{file_jsone}'

    try: # Создание новой директории если папка new_directory отсутствует
        os.mkdir(full_direc)
    except:
        pass

    
    data_dict:dict ={}
    id_list = []

    if (file_jsone not in os.listdir(full_direc)):
        for num in range(1,8):
            data_dict[str(num)] = {}
    else:
        with open(full_name_file_json, 'r', encoding='utf-8') as f:
            data_dict = json.load(f)
        for val in data_dict.values():
            for key2 in val.keys():
                id_list.append(key2)       
    
    while True:
        os.system ('cls')
        print(data_dict)
        print(id_list)
        name = input('Ввод имени.\nДля выход введите q и Enter.\nВведите имя:')
        if (name == 'q'):
            break
        while True:
            id_name = str(input_number_min(number_min=0,text='Введите ID от 0 до бесконечности:')) # Ввод ID имени
            if(id_name in id_list):
                print(f'ID существует, введите его заново!')
                continue
            else:
                break
        id_list.append(id_name)

        access_level = str(input_number_min_max(number_min= 1, number_max=7, text='Введите уровень доступа от 1 до 7: '))

        data_dict[access_level][id_name] = name

    with open(full_name_file_json, 'w', encoding='utf-8') as f_json:
        json.dump(data_dict,f_json, indent=2, separators=(',', ':'))
        
