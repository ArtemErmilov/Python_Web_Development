# Задание №5
# 📌 Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# 📌 загрузка данных (функция из задания 4)
# 📌 вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# 📌 добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.

from Path_File import PathFile

import json
import os

# Задание №4
# 📌 Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# 📌 Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# 📌 Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.

from Path_File import PathFile

from Pra_less13_task4 import *

import json
import os


class Loger:

    db ={}

    def __init__(self):
       self.__class__.db = load_json(__file__)

    def _authorize (self,*, the_id=None, name=None):
        if (the_id==None or name == None):
            print('Авторизация пользователяЖ')
            if (the_id==None):
                the_id = int(input('Введите личный идентификатор: '))
            
            if (name == None):
                name = input('Введите имя: ')

        if str(the_id) in self.__class__.db and self.__class__.db[str(the_id)]['name'] == name:
            
            self.level_authorize = self.__class__.db[str(the_id)]['level']
            return self.level_authorize
        else:
            raise Exception('Пользователь с такими данными не найден!')       

    def new_user(self,*,new_id:int = None, new_name:str = None):
        authorize_level =  self._authorize(the_id = new_id, name = new_name)
        user = worker()

        if (str(user.the_id) in self.__class__.db):
            raise Exception('Пользователь с этим ID уже записан в базу')

        if (user.level > authorize_level):
            raise ValueError (f'Введённый уровень доступа {user.level} выше уровня авторизации {authorize_level}')
        
        self.__class__.db[user.the_id] = {'name': user.name,'level': user.level}

        save_json(self.__class__.db,__file__)
        



if __name__ == '__main__':
    while True:
        num = int(input('Введите что вы будете делать 1 - ввод данных, 2 - вход под уровнем доступа, всё остальное выход.'))
        if (num == 1):
            user_db = load_json(__file__)
            new_user = worker()
            if str(new_user.the_id) in user_db:
                raise Exception('Пользователь с этим ID уже записан в базу')
            else:
                user_db[new_user.the_id] = {'name': new_user.name,'level': new_user.level}
            save_json(user_db,__file__)
            continue

        elif(num == 2):

            loger = Loger()
            loger.new_user(new_id = 1,new_name='Артём')
            continue
        
        else:
            break   
