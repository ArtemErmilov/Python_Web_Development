

import csv
from functools import wraps
import os
from typing import Callable


def dec_solution_csv(func:Callable, *,diretc:str = 'Python\Homework\HW9',\
                name_new_direct:str = 'HW9_task1', name_file:str = 'HW9_task1_csv.csv'):
    dict_list = {}
    @wraps(func)
    def wrapper(*args,**kwargs):
        nonlocal diretc,name_new_direct,name_file,dict_list
        full_direct = os.path.join(diretc,name_new_direct)
        full_name = os.path.join(full_direct, name_file)

        with open(full_name,'r',encoding='utf-8') as f_csv_read:
            csv_file = csv.reader(f_csv_read,dialect='excel',delimiter='|')
            for a,b,c in csv_file:
                a,b,c = int(a), int(b),int(c)
                
                if(a==0):
                    a1 = ''
                else:
                    a1 = f'{a}x2'
                if(b<0):
                    b1 = f'{b}x'
                elif(b==0):
                    b1 = ''
                else:
                    b1 = f'+{b}x'
                if(c<0):
                    c1 = f'{c}'
                elif(c==0):
                    c1 = ''
                else:
                    c1 = f'+{c}'
                dj = a1+b1+c1+'=0'
                data = func(a,b,c)
                dict_list[dj] = data
        return dict_list
    return wrapper