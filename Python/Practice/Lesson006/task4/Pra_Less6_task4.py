# Задание №4

# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и 
# количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, 
# если попытки исчерпаны.

from random import randint as ran, choice as ch

def mystery (text_my,answer:list, count:int = 5):
    answer = list(map(lambda x: x.lower(),answer))
  
    for cou in range(1,count+1):
        ans = input(f'{text_my} Ответ: ').lower()
        if (ans in answer):
            return cou
    return 0
