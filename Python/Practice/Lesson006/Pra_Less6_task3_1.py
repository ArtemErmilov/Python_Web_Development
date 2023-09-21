# Задание №3

# Улучшаем задачу 2.

# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте 
# генераторное выражение.

from sys import argv

from task2 import find

options = argv[1:]


if len(options)==1:
    _,min_num = options
    max_num = 100
    cont = 10
elif len(options)==2:
    _,min_num,max_num = options
    cont = 10
else:
    _,min_num,max_num, cont,*_ = argv

find(int(min_num),int(max_num),int(cont))