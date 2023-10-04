# Задание №4
# 📌 Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой
# функции.

from typing import Callable
from functools import wraps

def count (num: int = 1):
    def deco(func:Callable):
        @wraps(func)
        def wrapper(*args,**kwargs):
            res = []
            for _ in range(num):
                
                res.append(func(*args,**kwargs))
            return res
        return wrapper
    return deco

@count(5)
def fibonacci (number:int):
    result = 0
    new_new_number = 0
    
    for i in range(2,number+1):
        new_number = result
        if (i == 2):
            result = 1
        else:
            result = new_number + new_new_number
            new_new_number = new_number

    return result

