# Задача 2
# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

def cont(a,b):
    """
    Функция сокращения дроби.
    a - числитель,
    b - знаменатель.
    """
    c, a =  divmod(a,b) 
    if (a==0):
        return str(c)
    else:
        temp = a
        while temp != 1:
            if b % temp == 0:
                a = a//temp
                b = b//temp
                temp = a
                continue
            temp -=1
    if (c == 0):
        return(str(a)+'/'+str(b))
    else:
        return(str(c) + ' ' + str(a) + '/' + str(b))

def cont_new(a,b):
    """
    Функция сокращения дроби.
    a - числитель,
    b - знаменатель.
    """
    c, a =  divmod(a,b) 
    if (a==0):
        return str(c)
    else:
        dew = a
        temp = b
        while temp:
            dew, temp = temp,dew % temp
        a = a//dew
        b = b //dew
    if (c == 0):
        return(str(a)+'/'+str(b))
    else:
        return(str(c) + ' ' + str(a) + '/' + str(b))

print('Введите 2-а дробных числа в виде "a/b", где a - числитель, b - знаменатель.')

a1 = int(input('Введите числитель первого числа: '))
b1 = int(input('Введите знаменатель первого числа: '))

a2 = int(input('Введите числитель второго числа: '))
b2 = int(input('Введите знаменатель второго числа: '))


# Нахождение суммы дробных чисел

sum_a = a1 * b2 + a2 * b1
sum_b = b1 * b2


mul_a = a1 * a2
mul_b = b1 * b2

print (f'Сумма чисел "{a1}/{b1}" и "{a2}/{b2}" равна "{cont(sum_a,sum_b)},{cont_new(sum_a,sum_b)}",{sum_a= },{sum_b = }')
print (f'Произведение чисел "{a1}/{b1}" и "{a2}/{b2}" равна "{cont(mul_a,mul_b)}",{cont_new(mul_a,mul_b)}')