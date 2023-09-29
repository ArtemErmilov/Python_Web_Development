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

def read_pickle(directory:str):    

    with open(directory,'rb') as pickle_file:
        data = pickle.load(pickle_file)
    print(data)

