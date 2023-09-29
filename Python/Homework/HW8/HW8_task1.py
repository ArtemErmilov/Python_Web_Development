# Задание
# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# 📌 Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

import copy
import csv
import json
import os
from pathlib import Path
import pickle

def get_size(path:str)->int:
    """
    Функция get_size определяет размер папки path со всеми вложениями в байтах
    path:str - имя папки, которой необходимо определить размер.
    """
    size = 0
    for dir_path, _, file_names in os.walk(path):
        for f in file_names:
            fp = os.path.join(dir_path, f)
            size += os.path.getsize(fp)
    return size



def file_viewer(path:str,file_name:str = 'data_path'):
    """
    Функция которая рекурсивно проходит по всем папки, по всем вложенным папка и их файлам,
    определяет путь до объекта, тип объекта, размер объекта . Все собранные данные записываются 
    в файл file_name с расширение json, csv и pickle.
    """

    name_json_file = f'json_{file_name}.json'
    full_name_json_file = os.path.join(path, name_json_file)

    name_csv_file = f'csv_{file_name}.csv'
    full_name_csv_file = os.path.join(path, name_csv_file)

    name_pickle_file = f'pickle_{file_name}.pickle'
    full_name_pickle_file = os.path.join(path, name_pickle_file)

    path_list = os.walk(path)

    result = {}

    result_csv = []

    for dir_path, dir_name, file_name in  path_list:

        p = file_name + dir_name

        result[dir_path] = []

        for obj in p:
            size = 0
            name = obj
            obj = os.path.join(dir_path, obj)

            if(os.path.isdir(obj)):
                text = 'Папка'
                size = get_size(obj)
            elif(os.path.isfile(obj)):
                text = 'Файл'
                size = os.path.getsize(obj)
            elif(os.path.islink(obj)):
                text = 'Ссылка'
            else:
                text ='Не определено'
            result.get(dir_path).append([{name:[text,size]}])
            result_csv.append([dir_path,name,text,size])

    with open (full_name_json_file,'w',encoding= 'UTF-8') as f_json,\
        open(full_name_csv_file,'w',encoding='UTF-8') as f_csv,\
         open(full_name_pickle_file, 'wb') as f_pickle:

        json.dump(result,f_json, indent=4, separators=(',',':'),ensure_ascii= False)

        csv_writer = csv.writer(f_csv,dialect='excel',  delimiter='|')
        for data in result_csv:
            csv_writer.writerow(data)
            
        pickle.dump(result, f_pickle)        

    return result

    


    

direct = 'Python/Homework'

print(file_viewer(direct ))





  


