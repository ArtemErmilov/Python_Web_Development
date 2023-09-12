# Задание №4
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

from pprint import *

my_list = [2,3,8,21,2,19,19,3,2,4,3,8,2,21,6,20,20,7]
print(my_list)

DIV = 2

i = 0

while i < len(my_list):
    item = my_list[i]
    if(cou := my_list.count(item)) >= DIV :
        if (cou%DIV):
            cou-=cou%DIV
        for _ in range(cou):
            my_list.remove(item)
        continue
    i += 1

print(my_list)
