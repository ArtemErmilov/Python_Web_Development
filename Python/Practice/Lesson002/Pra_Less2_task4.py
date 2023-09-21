# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

from cmath import pi
from decimal import *
import decimal

decimal.getcontext().prec = 42
diameter = 1001

while diameter > 1000:
    diameter = Decimal(input('Введите диаметр: '))

s = Decimal(pi) * (diameter/2)**2
l = Decimal(pi) * diameter

print(f' Площадь круга = {s}')
print(f' Периметр круга = {l}')
