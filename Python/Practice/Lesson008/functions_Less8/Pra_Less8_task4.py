# Задание №4
# 📌 Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# 📌 Дополните id до 10 цифр незначащими нулями.
# 📌 В именах первую букву сделайте прописной.
# 📌 Добавьте поле хеш на основе имени и идентификатора.
# 📌 Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# 📌 Имя исходного и конечного файлов передавайте как аргументы
# функции.

import csv
import json
import os


def file_creation_csv_json(directory:str, new_directory:str,*,name_file_csv:str,name_file_json:str):
    """
    Функция, которая берёт данные из scv фала и преобразует его в json.
    Дополните id до 10 цифр незначащими нулями.
    В именах первую букву сделайте прописной.
    Добавьте поле хеш на основе имени и идентификатора.
    Получившиеся записи сохраните в json файл, где каждая строка
    csv файла представлена как отдельный json словарь.

    directory:str - путь до директории где создаётся новая папка new_directory.
    name_file_csv:str - имя исходного файла csv без расширения csv.
    name_file_json:str - имя файла json без расширения json.
    """
    full_direc = f'{directory}/{new_directory}' #Директория  с новой папкой

    file_csv = f'{name_file_csv}.csv' 
    full_name_file_csv = f'{directory}/Pra_Less8_task3/{file_csv}' # csv

    file_json = f'{name_file_json}.json' # json
    full_name_file_json = f'{full_direc}/{file_json}'

    try: # Создание новой директории если папка new_directory отсутствует
        os.mkdir(full_direc)
    except:
        pass
    
    json_file = {}

    if (file_csv in os.listdir(f'{directory}/Pra_Less8_task3')):

        with open(full_name_file_csv, 'r', newline='',encoding='UTF-8') as f:
            csv_file = csv.reader(f, dialect='excel',delimiter='|')

            for name, id_name, ac_lev in csv_file:
                #id_name = ('0'*10+id_name)[-10:]
                id_name = id_name.zfill(10)
                name = name.title()
                hash_name = hash(name+id_name)
                json_file[hash_name] = [name, id_name, ac_lev]
                # temp = [{id_name:name},hash_name]
                # if (json_file.get(ac_lev)==None):
                #     json_file[ac_lev] = [temp]
                   
                # else:
                #     json_file.get(ac_lev).append(temp)
    else:
        print('Файл не существует!')
        return    

    with open(full_name_file_json, 'w', encoding='utf-8') as f_json:
        json.dump(json_file,f_json, indent=4,ensure_ascii=False, separators=(',', ':'))
            
    