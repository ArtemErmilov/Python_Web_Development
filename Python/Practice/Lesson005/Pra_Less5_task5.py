# Задание №5
# ✔ Напишите программу, которая выводит на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.


# if (i % 3 == 0 and i % 5 == 0): i = 'FizzBuzz'; elif (i % 3 == 0): i = 'Fizz'; elif (i % 5 == 0): i = 'Buzz'



for i in range(100):
    if (i % 3 == 0 and i % 5 == 0): 
        i = 'FizzBuzz'
    elif (i % 3 == 0): 
        i = 'Fizz'
    elif (i % 5 == 0): i = 'Buzz'

    print(i)

gen_num =('FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else i  for i in range(101)  )

while True:
    try:
        print(next(gen_num))
    except:
        break