# Функции locals(), globals(), vars()
# И в финале несколько функций о переменных и областях видимости.

# Функция locals()

# Функция возвращает словарь переменных из локальной области видимости на
# момент вызова функции.

SIZE = 10

def func(a, b, c):
    x = a + b
    print(locals())
    z = x + c
    return z
func(1, 2, 3)

# Функция globals()

# Функция возвращает словарь переменных из глобальной области видимости, т.е. из
# пространства модуля.
SIZE = 10
def func(a, b, c):
    x = a + b
    print(globals())
    z = x + c
    return z
print(globals())
print(func(1, 2, 3))

# Функция не сохраняет в словаре локальные переменные функций, даже если будет
# вызвана из тела функции.
# В словаре от globals содержаться и дандер переменные модуля. Они нужны Python
# для правильной работы кода.

x = 42
glob_dict = globals()
glob_dict['x'] = 73
print(x)

# Функция vars()

# Функция без аргументов работает аналогично функции locals(). Если передать в vars
# объект, функция возвращает его атрибут __dict__. А если такого атрибута нет у
# объекта, вызывает ошибку TypeError.

print(vars(int))

# Получили все дандер методы класса int