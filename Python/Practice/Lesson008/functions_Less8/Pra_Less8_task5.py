# Задание №5

# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import json
import os
import pickle

def json_to_pickle(directory:str, new_directory:str):
    
    full_direc = f'{directory}/{new_directory}'

    list_files = os.listdir(full_direc)
    
    list_json_files = []

    for files in list_files:
       
        if(files.endswith('.json')):
            list_json_files.append(files)
    
  
    
    for name_file_json in list_json_files:

        name_file,*_ = name_file_json.split('.')
        with open(f'{full_direc}/{name_file_json}', 'r', encoding='utf-8') as f_json,\
                open(f'{full_direc}/{name_file}.pickle', 'wb') as f_pickle:
               
                data_dict = json.load(f_json)

                pickle.dump(data_dict, f_pickle)
                