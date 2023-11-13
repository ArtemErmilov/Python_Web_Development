# Задание №2
# 📌 Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import os
from Path_File import PathFile

import json

class NewFactorial:

    f1 = PathFile(__file__)

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
    
    def __enter__(self): # Метод входа
       
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb): # Метод выхода
        new_directory = self.f1.get_name_file_no_exten()
        directory = self.f1.get_full_name_file_no_exten()
        name_directory =self.f1.get_path_file()
        if (new_directory not in os.listdir(name_directory)):
            os.mkdir(directory)
        
        full_name_json_file =f'{directory}\{self.f1.get_name_file_no_exten()}.json'

        file = open(full_name_json_file,'w',encoding='utf-8')
        json.dump(self.storage,file, indent = 4)
        file.close()

with NewFactorial(5) as fact:
 
    print(fact(6))
    fact(7)
    fact(8)
    fact(9)
  
    

