# # Словарь представляет набор пар
# # ключ-значение. Ключ — любой неизменяемый тип данных. Значение - любой тип
# # данных. Обращаясь к ключу словаря получают доступ к значению.

a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}# передать набор пар ключ-значение в фигурных скобках,
b = dict(one=42, two=3.14, ten='Hello world!')# использовать знак равенства между ключом и значением,
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])# передать любую последовательность, каждый элемент который пара ключ и значение
print(a == b == c)

#Добавление нового ключа

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
my_dict['ten'] = 10
print(my_dict)

#Доступ к значению словаря
#Доступ через квадратные скобки []

TEN = 'ten'
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict['two'])
print(my_dict[TEN])
print(my_dict[1]) # KeyError: 1

#Доступ через метод get

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))
print(my_dict.get('five')) # Если обратиться к несуществующему ключу, get возвращает None.
print(my_dict.get('five', 5)) # Метод get принимает второй аргумент, значение по умолчанию.
# Если ключ отсутствует в словаре, вместо None будет возвращено указанное значение.
print(my_dict.get('ten', 5))

# Метод setdefault
# Метод setdefault похож не get, но отсутствующий ключ добавляется в словарь.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five') # Добавляется ключ 'five' и аргумент None
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.setdefault('six', 6) # Добавляется ключ 'six' и аргумент 6
print(f'{eggs = }\t{my_dict=}')
new_spam = my_dict.setdefault('two') # Возвратиться по ключу 'two' аргумент 2
print(f'{new_spam=}\t{my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000) # Возвратиться по ключу 'one' аргумент 1, и изменения аргумента не 
#произойдёт, потому, что словари не изменяемы.
print(f'{new_eggs=}\t{my_dict=}')

# # Метод keys
# # Метод keys возвращает объект-итератор dict_keys.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.keys())
for key in my_dict.keys():
    print(key)


# Метод values
# Метод values похож на keys, но возвращает значения в виде объекта итератора
# dict_values, а не ключи.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.values())
for value in my_dict.values():
    print(value)


# Метод items
# Если в цикле необходимо работать одновременно с ключами и значениями, как с
# парами, используют метод items.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.items())
for tuple_data in my_dict.items():
    print(tuple_data)
for key, value in my_dict.items():
    print(f'{key = } value before 100 - {100 - value}')

# Если создать цикл for с одной
# переменной между for и in, получим кортеж из пар элементов — ключа и значения.
# Обычной используют две переменные в цикле: первая принимает ключ, а вторая
# значение.


# Метод popitem
# Для удаления пары ключ значение из словаря используют метод popitem.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.popitem()
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.popitem()
print(f'{eggs = }\t{my_dict=}')

# # Метод pop
# # Метод pop удаляет пару ключ-значение по переданному ключу.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.pop('two')
print(f'{spam = }\t{my_dict=}')
err = my_dict.pop('six') # KeyError: 'six'
err = my_dict.pop() # TypeError: pop expected at least 1 argument, got 0

# Метод update
# Для расширение словаря новыми значениями используют метод update.

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict.update(dict(six=6))
print(my_dict)
my_dict.update(dict([('five', 5), ('two', 42)]))# Обновление старых значений 'two': 2 на 'two': 45
# и добавление новых  ('five', 5)
print(my_dict)
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6) # так-же добавлять значения в словарь можно
# через |
print(new_dict)