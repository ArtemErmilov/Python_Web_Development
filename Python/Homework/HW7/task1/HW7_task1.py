# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

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
    new_directory: - название папки, которую надо создать.
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


def generator_multi_file_direc(directory:str,new_directory:str,list_dict:dict):
    """
    Функция генерирования файлов с разным расширением.
    directory - директория в которой надо создать папку.
    new_directory - название папки, которую надо создать.
    list_dict:dict - словарь где: ключ - расширение файла (формат str), 
    значение - количество файлов (формат int)
    """
        

    for key in list_dict.keys():
        value = list_dict[key]

        generator_file(directory,new_directory,extension=key,number_files=value)


def sorting_files(directory_sorting_files:str):
    """
    Функция сортировки файлов по папкам Music, Picture, Text
    в директории directory_sorting_files.
    """
    music_lisp_extension =['mp3','mp4','wav','wma','mpg','mpeg','wmv']
    music_lisp_extension = list(map(lambda x: x.lower(),music_lisp_extension))
    picture_lisp_extension = ['png','jpeg','bmp','gif','tiff']
    picture_lisp_extension = list(map(lambda x: x.lower(),picture_lisp_extension))
    text_lisp_extension = ['doc','docm','docx','dot','txt','pdf']
    text_lisp_extension = list(map(lambda x: x.lower(),text_lisp_extension))

    music_list = []
    picture_list = []
    text_list = []
    
    file_list = os.listdir(directory_sorting_files)
    
    for data in file_list:
        *_, exten =  data.split('.')
        exten = exten.lower()
        if (exten in music_lisp_extension):
            music_list.append(data)
        elif(exten in picture_lisp_extension):
            picture_list.append(data)
        elif(exten in text_lisp_extension):
            text_list.append(data)

    if (len(music_list)>0 and 'Music' not in file_list):
        os.mkdir(f'{directory_sorting_files}/Music')
    if (len(picture_list)>0 and 'Picture' not in file_list):
        os.mkdir(f'{directory_sorting_files}/Picture')
    if (len(text_list)>0 and 'Text' not in file_list):
        os.mkdir(f'{directory_sorting_files}/Text')
    
    list_dect = {'Music':music_list,'Picture':picture_list,'Text':text_list}
    
    for key in list_dect.keys():
        for name_file in list_dect[key]:
            old_file = Path(f'{directory_sorting_files}/{name_file}')

            new_file = old_file.replace(Path.cwd() / f'{directory_sorting_files}/{key}' / name_file)


        
    