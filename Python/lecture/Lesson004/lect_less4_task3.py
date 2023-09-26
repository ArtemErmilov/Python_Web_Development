# Аргументы функции
# Рассмотрим функцию с параметрами, т.е. принимающую на вход значения.
# Вспомним как в школе решали квадратные уравнения. Заодно разберём
# особенности создания функций в Python.

def quadratic_equations(a: int or float, b: int or float, c: int or float) -> tuple [float, float] or float or str:
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return 'Нет решений'        


def quadratic_equations_1(a: int or float, b: int ro float, c: int or float) -> tuple [float, float] or float or None:
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return None

print(quadratic_equations(2, -3, -9))       
print(quadratic_equations_(2, -3, -9))