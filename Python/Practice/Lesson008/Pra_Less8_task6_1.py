# Задание №6
# 📌 Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# 📌 Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.




import csv

import pickle

import json


directory = 'Python/Practice/Lesson008/Pra_Less8_task6'
name_f_pic = 'Pra_Less8_task4_json.pickle'
name_f_csv,*_ = name_f_pic.split('.')
name_f_csv = f'{name_f_csv}.csv'
full_name_f_pic= f'{directory}/{name_f_pic}'
full_name_f_csv = f'{directory}/{name_f_csv}'


def read_pickle(directory:str):    

    with open(directory,'rb') as pickle_file:
        data = pickle.load(pickle_file)
    return data

def create_csv_table(data_csv: dict):
    csv_headers = list(data_csv.keys())
    csv_table = list(data_csv.values())
    csv_table = list(zip(*csv_table))
    with open(full_name_f_csv,'w',encoding='utf-8') as file:
        csv_writer = csv.writer(file,dialect='excel',delimiter=' ')
        csv_writer.writerow(csv_headers)
        csv_writer.writerow(csv_table)

new_data = read_pickle(full_name_f_pic)

create_csv_table(new_data)

