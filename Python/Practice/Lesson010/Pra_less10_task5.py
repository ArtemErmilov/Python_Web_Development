# Задание №5
# 📌 Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Animals:
    
    def __init__(self, name: str, agy:int):
        self.name = name
        self.agy = agy
    
    def get_name(self):
        return self.name
    
    def get_agy(self):
        return self.agy

class Fish (Animals):

    def __init__(self, name: str, agy: int, scales:str ):
        super().__init__(name, agy)
        self.scales = scales
    
    def get_fish_scales (self):
        return f'Чешуя: {self.scales}'  
   
class Birds (Animals):

    def __init__(self, name: str, agy: int, feathers:str):
        super().__init__(name, agy)
        self.feathers = feathers
    
    def get_brigs_feathers(self):
        return f'Перья: {self.feathers}' 

class Reptiles(Animals):

    def __init__(self, name: str, agy: int,skin:str ):
        super().__init__(name, agy)
        self.skin = skin
    
    def get_reptiles_skin(self):
        return f'Кожа: {self.skin}'


f = Fish('Яна',2,'Блестящая')
b = Birds('Аргоша',3,'Волнистая')
r = Reptiles('Ползун',10, 'Чёрная')

