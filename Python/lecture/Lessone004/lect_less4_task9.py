# Области видимости: global и nonlocal
# ● локальная — код внутри самой функции, т.е. переменные заданные в теле
# функции.
# ● глобальная — код модуля, т.е. переменные заданные в файле py содержащем
# функцию.
# ● не локальная — код внешней функции, исключающий доступ к глобальным
# переменным.

#Локальные переменные:
def func(y: int) -> int:
    x = 100 # Локальная переменная, которая используется внутри функции, и не выходит наружу.  
    print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1
x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')


#Глобальные переменные:
def func(y: int) -> int:
    global x # Глобальная переменная, которая общается с внешними племенными в не тела функции
    x += 100
    print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1
x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')

#Не локальные переменные:
def main(a):
    x = 1
    def func(y):
        nonlocal x # выход за пределы функции, но не работает с глобальными переменными.
        x += 100
        print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
        return y + 1
    return x + func(a)

x = 42
print(f'In main {x = }')
z = main(x)
print(f'{x = }\t{z = }')

# Доступ к константам
# Один из случаев когда обращение из тела функции к глобальной переменной
# считается нормальным — доступ к константам.
LIMIT = 1_000

def func(x, y):
    result = x ** y % LIMIT
    return result

print(func(42, 73))