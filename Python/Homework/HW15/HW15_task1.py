# Домашнее задание 

# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.

# Соберите информацию о содержимом в виде объектов namedtuple.
#Каждый объект хранит: 
# ○ имя файла без расширения или название каталога, 
# ○ расширение, если это файл, 
# ○ флаг каталога, 
# ○ название родительского каталога.
# 📌В процессе сбора сохраните данные в текстовый файл используя логирование.

from Path_File import PathFile
import os

from collections import namedtuple
import logging

import argparse

file = PathFile(__file__).get_new_folder_full_name_file_new_exten('txt',add_to_name='logg')

logger = logging.getLogger(__name__)
my_format = '{msg}'
logging.basicConfig(filename=file,filemode='w', 
                    level=logging.INFO, style='{', format=my_format) # encoding = 'UTF-8'

def file_viewer_logger(path_file:str):

    path_list = os.walk(path_file) 
    Data_ffl = namedtuple('Data_ffl', ['type', 'name', 'arent_direc', 'extension'], defaults=[None, None, None,None])       

    for dir_path, dir_name, file_name in  path_list:

        p = file_name + dir_name

        
        for obj in p:
            
            obj = os.path.join(dir_path, obj)

            if(os.path.isdir(obj)):# Определяет, является ли файл папкой
                type_f = 'Папка'
                parent_direc = os.path.dirname(obj)
                dir_name = os.path.basename(obj)
                data_file = Data_ffl(type_f,dir_name,parent_direc)

            elif(os.path.isfile(obj)): #Определяет, является ли файл файлом
                type_f = 'Файл'
                parent_direc = os.path.dirname(obj)
                f_name,extension = os.path.splitext(os.path.basename(obj))                
                data_file = Data_ffl(type_f,f_name,parent_direc, extension)
           
            elif(os.path.islink(obj)): #Определяет, является ли файл ссылкой
                type_f = 'Ссылка'
                parent_direc = os.path.dirname(obj)
                link_name = os.path.basename(obj)
                data_file = Data_ffl(type_f,f_name,link_name)
              
            else:
                type_f ='Не определено'
                data_file = Data_ffl(type_f)
            if (data_file.extension):
                msg = f'Тип:{data_file.type}, Название:{data_file.name},  Родительский каталог:{data_file.arent_direc}'
            else:
                msg = f'Тип:{data_file.type}, Название:{data_file.name}, Расширение:{data_file.extension}  Родительский каталог:{data_file.arent_direc},'
            logger.info(msg)
            

if __name__ == '__main__':


    parser = argparse.ArgumentParser()
    parser.add_argument('link', metavar='links',nargs = "*", type=str) 
    args = parser.parse_args()
   
    print(' '.join(args.link))
       

    file_viewer_logger(' '.join(args.link))

    # r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Python Web Development\Python\Practice'