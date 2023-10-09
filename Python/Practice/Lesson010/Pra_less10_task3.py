# Задание №3
# 📌 Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class ManeData:

    def __init__(self,name:str,patronymic:str, surname:str,years:int):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self._years = years
    def full_name(self):
        return f'{self.surname} { self.name} {self.patronymic}'
    def birthday(self):
        self._years+=1
    def show (self):
        return  self._years


# md = ManeData('Артём', 'Сергеевич','Ермилов', 38)

# # print(md.full_name())
# # print(md.show())
# # md.birthday()
# # md.birthday()
# # print(md.show())