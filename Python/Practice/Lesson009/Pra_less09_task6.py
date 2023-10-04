# Задание №6
# 📌 Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.


# Задание №5
# 📌 Объедините функции из прошлых задач.
# 📌 Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# 📌 Выберите верный порядок декораторов.

from Pra_less09_task3 import main as js_dec # декораторами для сохранения параметров

from Pra_less09_task2 import main as param_control_decor # декоратором контроля значений

from Pra_less09_task4 import count #декоратором для многократного запуска



@js_dec
@count(2)
@param_control_decor
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
                return True
            repet -=1
    
    print(f'Вы не угадали число!!! Заданное число {number}')
    return False
    

guessing_numbers(150,21)