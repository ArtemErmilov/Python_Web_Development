# from super_module import *
# SIZE = 49.5
# #print(f'{SIZE = }\n{result = }')
# #print(f'{z = }') # NameError: name 'z' is not defined
# print(f'{_secret = }') # NameError: name '_secret' is not defined
# print(f'{func(100, 200) = }\n{randint(10, 20) = }')

# def func(a: int, b: int) -> int:
#     return a + b
# print(f'{func(100, 200) = }')



import base_math
x = base_math.mul # Плохой приём
y = base_math._START_MULT # Очень плохой приём
z = base_math.sub(73, 42)
print(x(2, 3))
print(y)
print(z)