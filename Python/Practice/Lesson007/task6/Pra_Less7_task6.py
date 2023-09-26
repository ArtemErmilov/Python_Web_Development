# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


import os
import random
from string import ascii_lowercase

from pathlib import Path



vowel_letters_set = set('euioa')
consonants_letters_set = set (ascii_lowercase).difference(vowel_letters_set)

def random_name (min_len_name:int=4,max_len_name:int = 7):
    """
    Создание случайного имени из латинских букв длиной
    от min_len_name до max_len_name включительно.
    """
    

    len_name = random.randint(min_len_name,max_len_name+1)
    name = ''

    for i in range(len_name):
        name += random.choice(list(vowel_letters_set)) if i%2 else random.choice(list(consonants_letters_set))
    
    return name.title()




def generator_file(directory:str, new_directory:str, *,extension:str = 'txt',min_len_name:int = 6, max_len_name:str = 30,
                    min_bytes:int = 256,max_bytes:int = 4096,number_files:int = 42):

    """
    Программа для генерации файлов расширения extension в папку directory/new_directory
    directory: - директория в которой надо создать папку.
    new_directoryЖ - название папки, которую надо создать.
    min_len_name: - минимальное имя файла из латинских букв.
    max_len_name: - максимальное имя файла из латинских букв.
    min_bytes: - минимальное количество байт записанных в файл.
    max_bytes: - максимальное количество байт записанных в файл.
    number_files: - количество файлов, которые надо сгенерировать.
    """
    
    directory_new = f'{directory}/{new_directory}'

    if (new_directory not in os.listdir(directory)):
        os.mkdir(directory_new)
     

    
    list_name_file = [random_name(min_len_name,max_len_name) for _ in range(number_files)]    

   
    for name_file in list_name_file:
        with open(f'{directory_new}/{name_file}.{extension}', 'a+b')as f:
                f.write(bytearray(random.randint(min_bytes,max_bytes)))


def generator_multi_file_direc(directory: str,new_directory,list_dict:dict):
    """
    Функция генерирования файлов с разным расширением.
    directory - директория в которой надо создать папку.
    new_directory - название папки, которую надо создать.
    list_dict:dict - словарь где: ключ - расширение файла (формат str), 
    значение - количество файлов (формат int)
    """
    directory_new = f'{directory}/{new_directory}'
    
        
    if (new_directory not in os.listdir(directory)):
        os.mkdir(directory_new)
       

    for key in list_dict.keys():
        value = list_dict[key]

        generator_file(directory_new,f'file_{key}',extension=key,number_files=value)
