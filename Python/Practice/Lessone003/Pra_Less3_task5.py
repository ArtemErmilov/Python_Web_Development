# Задача №5
# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# Нумерация начинается с единицы.

import random


my_list = []

item_list = []

for _ in range (20):
    my_list.append(random.randint(1,10))

print (my_list)

for i, num in enumerate(my_list):
    if num%2:
        item_list.append(i+1)
print(item_list)