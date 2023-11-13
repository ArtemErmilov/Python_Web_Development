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

import json
import os


class User:
    def __init__(self, name: str, the_id: int, level:int = 1, authorize_level:str = 8):
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError('Имя должно быть текстового вида')
        self.name = name
        if not isinstance(the_id, int) or the_id <= 0:
            raise ValueError('Личный идентификатор должен быть целым числом')
        self.the_id = the_id
        if not isinstance(level, int) or level not in range(1, authorize_level):
            raise ValueError(f'Уровень доступа должен быть целым числом от 1 до {authorize_level}')
        self.level = level

    def __str__(self):
        return f'{self.name = }, {self.the_id = }, {self.level = }'
    
    def __eq__(self, other):
        return self.name == other.name and self.the_id == other.the_id

    def __hash__(self):
        return hash(self.name) + hash(self.the_id)


def load_json(file):
    f1 = PathFile(file)
    new_directory = f1.get_name_file_no_exten()
    directory = f1.get_full_name_file_no_exten()
    name_directory =f1.get_path_file()
    path = f'{directory}/{new_directory}_json.json'
    if (new_directory not in os.listdir(name_directory)):
        os.mkdir(directory)

    if os.path.exists(path):
        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
    else:
        data = {}
    return data


def worker():
    while True:
        try:
            name = input('Введите имя: ')
            the_id = int(input('Введите личный идентификатор: '))
            level = int(input('Введите уровень доступа: '))
            return User(name, the_id, level)
        except ValueError as e:
            print(e)


def save_json(user_db,file):

    f1 = PathFile(file)
    new_directory = f1.get_name_file_no_exten()
    directory = f1.get_full_name_file_no_exten()
    name_directory =f1.get_path_file()
    path = f'{directory}/{new_directory}_json.json'

    if (new_directory not in os.listdir(name_directory)):
        os.mkdir(directory)
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(user_db, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    
    user_db = load_json(__file__)
    new_user = worker()
    if str(new_user.the_id) in user_db:
        raise Exception('Пользователь с этим ID уже записан в базу')
    else:
        user_db[new_user.the_id] = {'name': new_user.name,'level': new_user.level}
    save_json(user_db,__file__)

