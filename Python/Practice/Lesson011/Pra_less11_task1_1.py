# Задание №1
 
# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания
# (time.time)

from datetime import datetime
class Duck:
    def __init__(self) :
        pass

class MyStr(str):

    def __new__ (cls,_class, author:str,value):
        instance = _class(value)
        return instance

    def __init__(self,_, value ):
        self.name = value   

a = MyStr(Duck,'ddfd54')

print(a)
