#ДЗ 9. Декораторы. 

# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.

from HW9_task1 import gen_num_ran

from HW9_task2 import dec_solution_csv

from HW9_task3 import dec_wr_json

import decimal

import math




@dec_wr_json
@dec_solution_csv
def quad_equation (a:int = 0, b:int = 0, c: int = 0):
    """
    Нахождение дискриминанта квадратного уравнения
    """
    a,b,c = decimal.Decimal(a), decimal.Decimal(b),decimal.Decimal(c)
    d2:decimal = b**2-4*a*c
    d:decimal = 0
    if (d2<0):
        return None        
    elif(d2 == 0):
        return float(round(decimal.Decimal(-1*b/(2*a)),5))
    else:
        d = decimal.Decimal(math.sqrt(d2))
    

    x1 = round((-1*b+d)/(2*a),5)
    x2 = round((-1*b-d)/(2*a),5)

    return float(x1),float(x2) 



#print(quad_equation(3,2,-10))
gen_num_ran(-100,100,100,name_file = 'HW9_task1_csv',name_new_direct = 'HW9_task1')

quad_equation ()
