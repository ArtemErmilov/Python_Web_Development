# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

text = 'Текст выравнивается по правому краю так, чтобы у самого длинного слова был один'\
                'пробел между ним и номером строки.'

text_list = text.split()
text_list.sort()
print (text_list)

light = 0



light = len(max(text_list, key=len))+1 # Нахождение самого длинного слова

for i, text in enumerate(text_list):
    print(f'{i}{text:>{light}}')