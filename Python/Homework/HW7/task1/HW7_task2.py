# Задача 1

# ✔ Напишите функцию группового переименования файлов. Она должна:
#    ✔ принимать параметр желаемое конечное имя файлов.
#       При переименовании в конце имени добавляется порядковый номер.
#    ✔ принимать параметр количество цифр в порядковом номере.
#    ✔ принимать параметр расширение исходного файла.
#        Переименование должно работать только для этих файлов внутри каталога.
#    ✔ принимать параметр расширение конечного файла.
#    ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
#       [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
#       желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os

def rename_file(directory:str,*, nem_final:str = '',letter_range:list = [],number_digits:int = 2,extension:list):
    direct_list = os.listdir(directory)
    if(len(letter_range)>0):
        if (len(letter_range)==1):
            a = 0
            b = letter_range[0]
        elif(min(letter_range)<0):
            b = min(letter_range)
            a = max(letter_range)    
        else:
            a = min(letter_range)
            b = max(letter_range)

    for ext in extension:
        i = 1
        for old_name in direct_list:
            old_name_spl, exten =  old_name.split('.')
            if exten == ext:
                number:str = ('0'*number_digits+str(i))[ -number_digits:]
                print(old_name)
                if(len(letter_range)==0):
                    new_name = f'{old_name_spl}{nem_final}{number}.{ext}'
                else:
                    new_name = f'{ old_name_spl[a:b] }{ nem_final }{ number }.{ ext }'
                print(new_name)
                os.rename(f'{directory}/{old_name}',f'{directory}/{new_name}')
                i += 1