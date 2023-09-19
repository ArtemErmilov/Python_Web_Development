from random import randint

__all__ = ['func', '_secret'] # Для работы с импортом через звёздочку (*)

SIZE = 100
_secret = 'qwerty'
__top_secret = '1q2w3e4r5t6y'

def func(a: int, b: int) -> str:
    z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
    return z
result = func(1, 6)

# В модуле есть следующие объекты:
# ● глобальная функция randint
# ● глобальная константа SIZE
# ● глобальная защищенная переменная _secret
# ● глобальная приватная переменная __top_secret
# ● глобальная функция func
# ● локальные параметры функции a и b
# ● локальная переменная функции z
# ● глобальная переменная result
