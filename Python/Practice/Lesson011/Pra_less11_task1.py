# Задание №1
 
# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания
# (time.time)

import time
from datetime import datetime

class MyStr(str):

    def __new__ (cls,value, author:str):
        instance = super().__new__(cls,value)
        cls.value = value
        cls.author = author
        cls.create_time = datetime.now()       
        return instance
    
    def __str__(self):
        return f'Автор: {self.author}, Время создания: {self.create_time.strftime("%Y-%m-%d %H:%M")}'

    def __repr__(self):
        return f'{self.value}, {self.author}'



class MyStr(str):
    """
    Класс для создания строки с информацией об авторе и времени создания.

    Атрибуты:
    value (str): строковое значение.
    author (str): имя автора.

    Dunder методы:
    __new__(cls, value, author): создает новый объект класса.
    __str__(): возвращает строковое представление объекта класса.
    __repr__(): возвращает строковое представление объекта класса для отладки.

    """
class MyStr(str):

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance

    def __str__(self):
        formatted_time = datetime.fromtimestamp(self.time).strftime('%Y-%m-%d %H:%M')
        return f"{super().__str__()} (Автор: {self.author}, Время создания: {formatted_time})"

    def __repr__(self):
        return f"MyStr('{super().__str__()}', '{self.author}')"


       


event = MyStr("Завершилось тестирование", "John")
print(event)

my_string = MyStr("Мама мыла раму", "Маршак")
print(repr(my_string))

