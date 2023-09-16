# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def key_parameters(**kwargs):
    new_dict = {}
    for value, key in kwargs.items():
        if hash(key)==key:
            key = str(key)
        new_dict[key] = value
    return new_dict

print (key_parameters(Возраст=39, Пол='М', Рост=180, Вес=95, Семейное_положение='В разводе'))