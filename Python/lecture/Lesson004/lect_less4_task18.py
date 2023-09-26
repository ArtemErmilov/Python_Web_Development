# 
# Функция all()

# all(iterable)
# Функция возвращает истину, если все элементы последовательности являются
# истиной. На Python создание функции all выглядело бы так:


def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

numbers = [42, -73, 1024]
if all(map(lambda x: x > 0, numbers)):
    print('Все элементы положительные')
else:
    print('В последовательности есть отрицательные и/или нулевые элементы')

# Функция any()

# any(iterable)
# Функция возвращает истину, если хотя бы один элемент последовательности
# являются истиной. На Python создание функции any выглядело бы так:

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

numbers = [42, -73, 1024]
if any(map(lambda x: x > 0, numbers)):
    print('Хотя бы один элемент положительный')
else:
    print('Все элементы не больше нуля')