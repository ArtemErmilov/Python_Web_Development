# Задание №6
# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

import random



def sum_list(number_list:list, i_min:int, i_max:int)->int:
    if (i_min < 0 ):
        i_min = 0
    if (i_max >= len(number_list)):
        i_max = len(number_list)
    
    return sum([number_list[i] for i in range(i_min,i_max+1)])

def sum_list_new(number_list:list, i_min:int, i_max:int)->int: # Задача с семинара
    i_min,i_max = sorted([i_min,i_max])
    
    return sum(number_list[i_min:i_max+1])

number_list = [random.randint(1,10) for _ in range(20)]

print(number_list)

print (sum_list_new(number_list,0,10))