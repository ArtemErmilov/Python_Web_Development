# # x = int("42")
# # y = int(3.1415)
# # z = int("hello", base=30)
# # print(x, y, z, sep='\n')

import sys


# STEP = 2 ** 16
# num = 1
# for _ in range(30):
#     print(sys.getsizeof(num), id(num), num)
#     num *= STEP

# num = 7_901_123_456_789

# num = 2 ** 16 - 1
# b = bin(num)
# o = oct(num)
# h = hex(num)
# print(b, o, h)


# print(0.1 + 0.2)
# pi = 3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375
# print(pi)


# DEFAULT = 42
# num = int(input('Введите уровень или ноль для значения по умолчанию: '))
# level = num or DEFAULT
# print(level)

# name = input('Как вас зовут? ')
# if name:
#     print('Привет, ' + name)
# else:
#     print('Анонимус, приветствую')


data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
while data:
    print(data.pop())

