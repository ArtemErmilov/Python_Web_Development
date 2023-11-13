# Задание №2
# 📌 Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются
#  в пару списков-архивов
# 📌 list-архивы также являются свойствами экземпляра

from copy import deepcopy


class MyArchive:
    _instance = []
    def __new__ (cls,number:int, text:str):
        instance = super().__new__(cls)
        instance.number = number
        instance.text = text
        instance.arch = cls._instance.copy()
        cls._instance.append(instance)
        return instance
    
    def __str__(self):
        return f'{self.number} {self.text} | {self.arch}'
    
    def __repr__(self):
        return f'{self.number} {self.text}'


a = MyArchive(1,'a')
b = MyArchive(2,'b')
c = MyArchive(3,'c')

print(a)
print(b)
print(c)