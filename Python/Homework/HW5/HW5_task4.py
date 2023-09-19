# Создайте функцию генератор чисел Фибоначчи (см. Википедию).


import copy 


def fibonacci(number):
    item = number
    result = 0
    number_temp = 0
    number_temp_old = 0
    while number != 0:
        number -= 1

        if item - 1 == number:
            yield result
        elif item - 2 == number:
            result = 1
            yield result
        else:
            number_temp_old = result #copy.copy(result)
            result += number_temp
            number_temp = number_temp_old #copy.copy(number_temp_old)           
            
            yield result


print (*fibonacci(20))
