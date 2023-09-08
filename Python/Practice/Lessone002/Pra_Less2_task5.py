# Задание №5
# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

import math
from math import *
from decimal import *
import decimal

print('Введите коэффициенты квадратного уравнения a*x2+b*x+c = 0')

a = float (input('Введите a: '))
b = float (input('Введите b: '))
c = float (input('Введите c: '))

de =  b**2 - 4*a*c

if 0 > de :
    de = complex (de)


x1 = ( - b + de ** 0.5 ) / (2 * a)

x2 = ( - b - de ** 0.5 ) / (2 * a)

if ( x1 == x2 ):
    print (f'Ответ х = {x1}')
else:
    print (f'Ответ х1 = {x1}, х2 = {x2}')

