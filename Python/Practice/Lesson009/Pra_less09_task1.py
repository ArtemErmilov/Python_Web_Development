# Задание №1
# 📌 Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

import random



def guessing_numbers ():
    number = random.randint(1,100)
    repet = random.randint(1,11)
    def repetitions_num():
        nonlocal number, repet
        for i in range(1,repet+1):
            num_in = int(input ('Введите число от 1 до 100: '))
            if (num_in > number):
                print(f'Вы ввели число БОЛЬШЕ загадочного. Осталось {repet-i} попыток.')
                continue
            elif (num_in < number):
                print(f'Вы ввели число МЕНЬШЕ загадочного. Осталось {repet-i} попыток.')
                continue
            else:
                print(f'Вы угадали число с {i} попытки!!!')
                break
        else:
            print(f'Вы не угадали число!!! Заданное число {number}')
        print('конец')    
        return
    return repetitions_num






