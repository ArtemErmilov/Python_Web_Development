# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

logger = logging.getLogger(__name__)

format = '{asctime:<20} - {levelname:<10} - {msg}'

logging.basicConfig(filename='Python\Practice\Lesson015\Pra_less15_task1.txt',filemode='w', 
                     level=logging.ERROR, style='{', format=format) # encoding = 'UTF-8'

def func_mat(a,b):
    try:
        return a / b
    except ZeroDivisionError as e:
        logger.error(msg=e)

func_mat (100,0)