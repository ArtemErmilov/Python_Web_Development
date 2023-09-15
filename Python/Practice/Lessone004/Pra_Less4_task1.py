# Задача 1
# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.



def text_print(text:str):
    text_list = text.split()
    
    text_list.sort()

    light = len(max(text_list, key=len))+1 # Нахождение самого длинного слова

    for i, text in enumerate(text_list):
        print(f'{i+1}{text:>{light}}')

   

    


text = 'Текст выравнивается по правому краю так, чтобы у самого длинного слова был один'\
                'пробел между ним и номером строки.'



text_print(text)

