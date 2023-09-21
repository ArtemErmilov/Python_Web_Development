# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

import random

number_list = [random.randint(1,10) for _ in range(10)]

def sort_bubble(num_list:list):
    for i in range(1,len(num_list)):
        for index in range(len(num_list)-i):
            if num_list[index+1]<num_list[index]:
                num_list[index],num_list[index+1] = num_list[index+1],num_list[index]
    

print(number_list)

sort_bubble(number_list)

print(number_list)
