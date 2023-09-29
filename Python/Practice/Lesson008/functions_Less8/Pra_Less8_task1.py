# Задание №1

# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.


import json
import os

from random import randint, uniform
import random
from string import ascii_lowercase



def wer_file_number(directory:str, new_directory:str,*,lines:int = 10,name_file:str):
    """
    Запись чисел файл в формате число1 | число 2
    directory: - путь до директории где создаётся новая папка new_directory
    lines: - количество записей в файл.
    name_file: - название файла
    """

    full_direc = f'{directory}/{new_directory}'

    try:
        os.mkdir(full_direc)
    except:
        pass

    dir_name_fi = f'{full_direc}/{name_file}'

   
    NUM_RAN_MIN = -1000
    NUM_RAN_MAX = 1000
    

    with open(dir_name_fi, 'w', encoding='utf-8') as f:
        for _ in range (lines+1):
            f.write(f'{randint(NUM_RAN_MIN,NUM_RAN_MAX+1)} | {uniform(NUM_RAN_MIN,NUM_RAN_MAX+1)}\n')


vowel_letters_set = set('euioa')
consonants_letters_set = set (ascii_lowercase).difference(vowel_letters_set)

def random_name (min_len_name:int=4,max_len_name:int = 7):
    """
    Создание случайного имени из латинских букв длиной
    от min_len_name до max_len_name включительно.
    """    
    min_len_name = min(min_len_name,max_len_name)
    max_len_name = max(min_len_name,max_len_name)

    len_name = random.randint(min_len_name,max_len_name+1)
    name = ''

    for i in range(len_name):
        name += random.choice(list(vowel_letters_set)) if i%2 else random.choice(list(consonants_letters_set))
    
    return name.title()

def wr_file_name(directory:str, new_directory:str,*,file_name:str,min_len_name:int=4,max_len_name:int = 7,number_line:int = 10):
    """
    Функция записи в файл с именем file_name случайных имён.
    directory: - путь до директории где создаётся новая папка new_directory
    file_name: - имя нового создаваемого файла.
    min_len_name: -  минимальное имя файла
    max_len_name: - максимальное имя файла
    number_line: - количество записей в файл.
    """

    full_direc = f'{directory}/{new_directory}'
    fuii_file_name = f'{full_direc}/{file_name}'

    try:
        os.mkdir(full_direc)
    except:
        pass
    with open(fuii_file_name, 'w', encoding='utf-8') as f1:
        for num in range(number_line):
               f1.write(f'{random_name(min_len_name,max_len_name)}\n')





def reading_file(directory:str, new_directory:str,*,file_num:str,file_name:str, new_name_file:str):
    
    directory = f'{directory}/{new_directory}'
    try:
        os.mkdir(directory)
    except:
        pass 


    file_num_new = f'{directory}/{file_num}'
    file_name_new = f'{directory}/{file_name}'
    new_name_file_new = f'{directory}/{new_name_file}'

    with    open(file_num_new, 'r', encoding='utf-8') as f_num,\
            open(file_name_new, 'r', encoding='utf-8') as f_name,\
            open( new_name_file_new, 'w', encoding='utf-8') as f_new_name:

        list_num = list(f_num)
        list_name = list(f_name)
        len_num = len(list_num)
        len_name = len(list_name)
        
        if (len_num>len_name):
            for i in range(len_num-len_name):
                list_name.append(list_name[i])
        else:
            for i in range(len_name-len_num):
                list_num.append(list_num[i])
        
        name_max_len = len(max(list_name))
       

        for num, name in zip(list_num,list_name):

            num1,num2 = num.split('|')
            num1,num2 = int(num1),float(num2)

            

            if (num1*num2<0):
                f_new_name.write(f'{name[:-2]}\t{abs(num1*num2)}\n')
            else:
                f_new_name.write(f'{name[:-2]}\t{round(num1*num2)}\n')


def file_creation_json(directory:str, new_directory:str,*,original_file_name:str,new_json_file_name:str):
    full_direc = f'{directory}/{new_directory}'
    full_original_file = f'{full_direc}/{original_file_name}'
    full_new_json_file = f'{full_direc}/{new_json_file_name}'

    with  open(full_original_file, 'r', encoding='utf-8') as f_orig,\
            open(full_new_json_file, 'w', encoding='utf-8') as f_json:

            orig_list = list(f_orig)
            list_dict ={}
            for data in orig_list:
                key,value = data.split()
                list_dict[key] = value

            json.dump(list_dict,f_json, indent=2, separators=(',', ':'))

                

