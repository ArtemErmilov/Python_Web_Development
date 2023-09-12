# f-строка
# Начиная с Python 3.7 для форматирования текста используют f-строки. Они
# работают быстрее, чем старые способы форматирования. А некоторые
# разработчики языка предлагают сделать их строками по умолчанию в одном из
# будущих релизов.
# f-строки похожи на более короткую и читаемую запись метода формат.

name = 'Alex'
age = 12
text = f'Меня зовут {name} и мне {age} лет'
print(text)

print(f'{{Фигурные скобки}} и {{name}}')

pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}') #Вывод данных с точностью до 2-х знаков после запятой
data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
    print(f'{item:>10}') # Отступ в право на 10 символов

num = 2 * pi * data[1]
print(f'{num = :_}') # Разбитие цифр на группы нижним подчёркиванием