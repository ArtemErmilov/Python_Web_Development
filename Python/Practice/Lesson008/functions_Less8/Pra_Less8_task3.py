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

# Задача 3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.



import csv
import os

from functions_Less8 import input_number_min, input_number_min_max


def personal_data_csv(directory:str, new_directory:str,*,name_file_json:str):
    """
    Функция считывает json файл и изымает из него данные. Потом принимает данные в ведённые с консоли
    Имя, ID - уникальные, проверяется, уровень доступа(1,7). Все данные после выхода
    из меню записывает в json файл.

    directory:str - путь до директории где создаётся новая папка new_directory
     name_file_json:str - имя файла json без расширения json
    """

    full_direc = f'{directory}/{new_directory}' #Директория  с новой папкой
    file_csv = f'{name_file_json}.csv'
    full_name_file_csv = f'{full_direc}/{file_csv}'

    try: # Создание новой директории если папка new_directory отсутствует
        os.mkdir(full_direc)
    except:
        pass

    
    data_dict:dict ={}
    id_list = []

    
    for num in range(1,8):
        data_dict[str(num)] = {}

    if (file_csv in os.listdir(full_direc)):
        with open(full_name_file_csv, 'r', newline='',encoding='UTF-8') as f:
            csv_file = csv.reader(f, dialect='excel',delimiter='|')
            for name, id_name, ac_lev in csv_file:
                id_list.append(id_name)
                data_dict[ac_lev][id_name] = name
   
    
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

    with open (full_name_file_csv, 'w', newline='',  encoding='utf-8') as f_csv:
        
        result =  []
        for ac_lev, users in data_dict.items():
            for id_name, name in users.items():
                result.append([name,id_name,ac_lev])
        
        csv_write = csv.writer(f_csv, dialect='excel',  delimiter='|', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerows(result)

        # csv_write = csv.DictWriter(f_csv, dialect='excel',  delimiter='|',fieldnames=['name','id_name','ac_lev'], quoting=csv.QUOTE_MINIMAL)
        # csv_write.writerows(data_dict)