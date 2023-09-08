#Задача 2.
# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

number = 0

while (1>number or number > 100000):
    number = int (input ('Введите число от 1 до 100 000 : '))

if (number == 1 or number == 2):
    print(f'Число {number} является простым!')

else:

    for num in range(2,number):

        if (number%num==0):
            print(f'Число {number} является составным!')
            break

        elif (num==number-1):
            print(f'Число {number} является простым!')

# Разбор ДЗ1

result = ''

if (number == 1 or number == 2):
   result = f'Число {number} является простым!'
elif (not number % 2):
    result = f'Число {number} является составным!'
else:
    for dev in range(3, number//2+1,2):
        if not number % dev:
            result = f'Число {number} является составным!'
            break
    else:
        result = f'Число {number} является простым!'
print(result)