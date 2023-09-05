# Задание №6

# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

year = int(input('Введите дату в формате yyyy: '))

greg_year = 1582
leap_year = 4
leap_year100 = 100
leap_year400 = 400

if year > greg_year:

    if year%leap_year == 0 : 
        if (year%leap_year100 == 0 ):
            if (year%leap_year400 == 0):
                print(f'Год {year} Високосный')
            else:
                print(f'Год {year} Не Високосный')
        else:
            print(f'Год {year} Не Високосный')
    else:
        print(f'Год {year} Не високосный')
else:
        print(f'Год {year} Не високосный')