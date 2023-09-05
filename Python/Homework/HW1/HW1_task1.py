# Задание №9 (Задача из семинара)
# 📌 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

from os import system

# system ('cls')  


c= ''

print()

for z in range (2):
    for x in range (2, 11):
        if z == 0:
            a = 2
            b = 6
        else:
            a = 6
            b = 10
        for y in range (a,b):
                c=c+ str(y) + ' x ' + str(x) + ' = ' + str(y*x) + '\t'
        print (c)
        c = ''
    print()