# Задание №2
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.


import logging
import os

from typing import Callable
from functools import wraps

def main (func:Callable):
    logger = logging.getLogger(__name__)
    format = '{msg}'
    logging.basicConfig(filename='Python\Practice\Lesson015\Pra_less15_task2.log',filemode='a', 
                            level=logging.INFO, style='{', format=format) # encoding = 'UTF-8'

    dict_data:dict = {}
    @wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        str_args, str_kwargs = '', ''
        if args:
            str_args  =('args:' + ', '.join(str(args)))
        if kwargs: 
            str_kwargs = 'kwargs:' +', '.join([f"{key} = {value}" for key, value in kwargs.items()])
        logger.info(msg=f'result:{result} ({str_args}) ({str_kwargs})')
            
        return result
    return wrapper

@main
def fibonacci (number:int, data: int):
    result = 0
    new_new_number = 0
    data +=1
    
    for i in range(2,number+1):
        new_number = result
        if (i == 2):
            result = 1
        else:
            result = new_number + new_new_number
            new_new_number = new_number

    return result 

if __name__== '__main__':
    print(fibonacci (10,50))
