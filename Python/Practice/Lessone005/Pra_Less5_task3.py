# Задание №3

# Продолжаем развивать задачу 2.
# Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

text = 'Самостоятельно сохраните в переменной строку текста.'



my_dict_new = {i: ord(i) for i in set(text)}

iter_my_dict_new = iter(my_dict_new.items())

for data in  range(5):
    print(next(iter_my_dict_new))

#print(*my_dict_new)
