# Задание №2

# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-
# угадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами
# из диапазонов.

from typing import Callable
import random
from functools import wraps

def main (func:Callable):
    @wraps(func)    
    def repetitions_num(number,repet):
        
        if ( number not in range(1,101)):
            print (f'Введёно число {number} не лежит в диапазоне от 1 до 100')
            number = random.randint(1,101)
        if ( repet not in range(1,11)):
            print (f'Введёно число {repet} не лежит в диапазоне от 1 до 10')
            repet = random.randint(1,11)
        return func(number,repet)
       
    return repetitions_num

@main
def guessing_numbers(number:int, repet:int):
    i = repet
    while repet:
            num_in = int(input ('Введите число от 1 до 100: '))
            if (num_in > number):
                print(f'Вы ввели число БОЛЬШЕ загадочного. У вас осталось {repet-1} попыток.')
                
            elif (num_in < number):
                print(f'Вы ввели число МЕНЬШЕ загадочного. У вас осталось {repet-1} попыток.')
                
            else:
                print(f'Вы угадали число с {repet-1} попытки!!!')
                break
            repet -=1
    else:
        print(f'Вы не угадали число!!! Заданное число {number}')
    return number, repet


