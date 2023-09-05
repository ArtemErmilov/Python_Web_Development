# Задание №9
# 📌 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

from os import system

system ('cls')  

print()

c= ''

for z in range (2):
    for x in range (2, 11):
        if z == 0:
            for y in range (2,6):
                c=c+ str(y) + ' x ' + str(x) + ' = ' + str(y*x) + '\t'
        else:
            for y in range (6,10):
                c=c+ str(y) + ' x ' + str(x) + ' = ' + str(y*x) + '\t'
        print (c)
        c = ''
    print()

        
        
    
