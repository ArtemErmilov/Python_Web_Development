# Работа в консоли в режиме интерпретатора Python.
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

n = int(input('Введите значение, до которого будет находится сумма чётных чисел => '))
e = int(input('Введите кратное число => '))
data = 0

for x in range(2,n,2):
    if x%e != 0:
        print(x)
        data = data + x

print(f'Сумма чисел от 1 до {n} равняется {data}')