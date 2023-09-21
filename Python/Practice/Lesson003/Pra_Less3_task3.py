# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:

# ключ — тип элемента,

# значение — список элементов данного типа.

from pprint import *

cor = 1, 2.0, 'text', [1,2,3], True, None, 2,
s_list = {}

for data in cor:
    if type(data) not in s_list:
        s_list[type(data)] = []

    s_list[type(data)].append(data)

new_s_list = {}

for data in cor:
    new_s_list.setdefault(type(data),[])
    new_s_list[type(data)].append(data)

pp (s_list)
print()
pp (new_s_list)