# Задание №4
# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

import random
from Pra_less10_task3 import ManeData

class Employee(ManeData):

    def __init__(self,id:int = None, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.id = id if id else random.randint(100000,1000000)
        self.access_level = self.get_access_level()
        
        

    def get_id(self):
        return self.id
    
    def get_access_level(self):
        return sum(list(map(int,str(self.id))))%7

men = Employee (None,'Артём', 'Сергеевич','Ермилов', 38)

print(men.get_id())
print(men.get_access_level())
print(men.full_name())
men.birthday()
print(men.show())
    