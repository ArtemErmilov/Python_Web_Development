# Задание №4

# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import os
import random
from string import ascii_lowercase





vowel_letters_set = set('euioa')
consonants_letters_set = set (ascii_lowercase).difference(vowel_letters_set)

def random_name (min_len_name:int=4,max_len_name:int = 7):
    

    len_name = random.randint(min_len_name,max_len_name+1)
    name = ''

    for i in range(len_name):
        name += random.choice(list(vowel_letters_set)) if i%2 else random.choice(list(consonants_letters_set))
    
    return name.title()




def generator_file(directory:str, new_directory:str, *,extension:str = 'txt',min_len_name:int = 6, max_len_name:str = 30,
                    min_bytes:int = 256,max_bytes:int = 4096,number_files:str = 42):
    """
    directory - директория в которой надо создать папку.
    new_directory - название папки, которую надо создать.

    """
    
    directory = f'{directory}/{new_directory}'
    try:
        os.mkdir(directory)
    except:
        pass   

    
    list_name_file = [random_name(min_len_name,max_len_name) for _ in range(number_files)]    

   
    for name_file in list_name_file:
        with open(f'{directory}/{name_file}.{extension}', 'w+b')as f:
                f.write(bytearray(random.randint(min_bytes,max_bytes)))      



