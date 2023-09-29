# Задание №5
# 📌 Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

from functions_Less8 import json_to_pickle

directory =  'Python/Practice/Lesson008'
new_directory = 'Pra_Less8_task4'

json_to_pickle(directory,new_directory)