# Задание №1
# 📌 Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

from collections import defaultdict


class MyFactorial:

    def __new__(cls, k:str = None ):
        instance = super().__new__(cls)
        if(k<1 or k == None):
             raise ValueError ('Значение K должно быть больше 0.')
        else:
            instance.k = k
        instance.storage = defaultdict(list)
        return instance

       
    def __str__ (self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
        return txt


    def __call__(self, value):  
        number = 1
        list_num = []
        for num in range(1,value + 1):
            number *=num
            if (num - (value - self.k)-1) >= 0:
                list_num.append(number)
            self.storage[value] = list_num
        return f'{value} : {list_num}'

class NewFactorial:

    def __new__(cls, k:str = None ):
        instance = super().__new__(cls)
        if(k<1 or k == None):
             raise ValueError ('Значение K должно быть больше 0.')
        else:
            instance.k = k
        instance.storage = {}
        return instance

    def _factorial(self, value):
        number = 1
        list_num = []
        for num in range(1,value + 1):
            number *=num
            list_num.append(number)
        return list_num
       
    def __str__ (self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
        return txt


    def __call__(self, value):  
        self.storage[value] = self._factorial(value)[-self.k:]
        return self.storage



f1 = NewFactorial(3)

print (f1(5))
f1(6)
f1(7)
print(f1)
    