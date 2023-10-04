import csv
import os
import random


def gen_num_ran(number_min:int,number_max:int, lines:int = 100,*,diretc:str = 'Python\Homework\HW9',\
                name_new_direct:str, name_file:str):
    """
    Запись чисел 3-х случайных чисел в одну строку и lines строчек и файл csv.
    """

    full_direct = os.path.join(diretc,name_new_direct)
    full_name = os.path.join(full_direct, f'{name_file}.csv')

    if ( name_new_direct not in os.listdir(diretc)):
        os.mkdir(full_direct)

    with open(full_name,'w',newline='',encoding='utf-8') as f_csv:

        csv_write = csv.writer(f_csv, dialect='excel', delimiter='|', \
                    quoting=csv.QUOTE_MINIMAL)
        for _ in range(lines):
            a:int = random.randint(number_min,number_max+1)
            b:int = random.randint(number_min,number_max+1)
            c:int = random.randint(number_min,number_max+1)
            csv_write.writerow([a,b,c])