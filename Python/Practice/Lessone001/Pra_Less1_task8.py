# Задание №8
# 📌 Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# 📌 Пример результата:
# Сколько рядов у ёлки? 5

from os import system

system ('cls')  

n = int(input ('Сколько рядов у ёлки: '))

a = ' '
b = '*'

iter = 1


for x in range(1,n+1):

    print(a*(n-x)+b*iter)
    
    iter+=2

for row in range(n): # 2-й вариант решения
    print(f'{"*"*(2*row+1):^{n*2+1}}')