# Задание №2

# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный
# по убыванию.

def text_to_unicode(text):
    text_list = sorted(set(text),reverse=True)
    uncod_list = []
    for data in text_list:
        uncod_list.append(ord(data))
    return uncod_list

text = 'Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный'

print(text_to_unicode(text))

print()

print([ord(i) for i in sorted(list(set(text)),reverse=True)])