def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the remainder of the division in the range [2, P).
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    >>> is_prime(3.14)
    Traceback (most recent call last):
    ...
    TypeError: The number P must be an integer type
    >>> is_prime(-100)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(100_000_001)
    If the number P is prime, the check may take a long time. Working...
    False
    >>> is_prime(100_000_007)
    If the number P is prime, the check may take a long time. Working...
    True
    """

    for i in range(2, p):
        if p % i == 0:
            return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Обратите внимание на многоточия в тестах ошибок. Модуль doctest ориентируется
# на первую строку об ошибке. Это или Traceback (most recent call last): или Traceback
# (innermost last): Так как номера строк кода, пути имена могут меняться, середина
# вывода игнорируется. Её можно заменить на многоточие. Важна последняя строка,
# которая начинается с типа ошибки и последующего за ней текста.
