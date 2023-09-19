# # Задание №1


# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым, если делится
# нацело только на единицу и на себя».


def prime_number (N):

    result = 1
    item = 0 

    while (item<N):
        result +=1   
        if (result == 2):
            item += 1
            yield result
        elif (result % 2==0):
            continue
        else:
            for dev in range(3, result//2+1,2):
                if not result % dev:
                    break
            else:
                item +=1
                yield  result  
            
        
for i, num in enumerate(prime_number(100), start=1):
    print(f'{i} = {num}')    
            