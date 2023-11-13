# Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.


import logging
import os

from typing import Callable
from functools import wraps

logger = logging.getLogger(__name__)
my_format = '{levelname:<20} - {asctime:<20} -{funcName} - {msg}'
logging.basicConfig(filename='Python\Practice\Lesson015\Pra_less15_task3.log',filemode='a', 
                             level=logging.INFO, style='{', format=my_format) # encoding = 'UTF-8'

def main (func:Callable):   

    
    @wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        delimiter = ', ' if args and kwargs else ''
        args_kwargs = f'{delimiter}'.join([f'args:{args}' if args else '', f'kwargs: {kwargs}' if kwargs else ''])
       
        logger.info(msg=f'result:{result}, {args_kwargs}')
            
        return result
    return wrapper

@main
def some_func(a: str, b: str):
    return a + '_' + b

if __name__== '__main__':
    some_func ('Pervi','Vtoroi')
    some_func ('Pervi',b='Vtoroi')
    some_func (a='Pervi',b='Vtoroi')
