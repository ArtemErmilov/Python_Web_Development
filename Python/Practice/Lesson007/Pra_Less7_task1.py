# Задание №1
# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform

def wer_file(*,lines:int = 10,name_file:str):

    directory = 'Python/Practice/Lesson007'

    dir_name_fi = f'{directory}/{name_file}'

   
    NUM_RAN_MIN = -1000
    NUM_RAN_MAX = 1000
    

    with open(dir_name_fi, 'a', encoding='utf-8') as f:
        for _ in range (lines+1):
            f.write(f'{randint(NUM_RAN_MIN,NUM_RAN_MAX+1)} | {uniform(NUM_RAN_MIN,NUM_RAN_MAX+1)}\n')        

    
wer_file(lines= 20, name_file='Pra_Less7_task1_data.txt')