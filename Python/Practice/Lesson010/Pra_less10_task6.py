# Задание №6
# 📌 Доработайте задачу 5.
# 📌 Вынесите общие свойства и методы классов в класс
# Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.

class Animals:
    
    def __init__(self, name: str, agy:int):
        self.name = name
        self.agy = agy
        self.spec =None

    def get_spec(self):
        return self.spec

class Dog(Animals):
    def __init__(self, name: str, agy: int, spec:str):
        super().__init__(name, agy) 
        self.spec = spec

class Cat(Animals):
    def __init__(self, name: str, agy: int, spec:str):
        super().__init__(name, agy) 
        self.spec = spec

class Birds(Animals):
    def __init__(self, name: str, agy: int, spec:str):
        super().__init__(name, agy) 
        self.spec = spec

c = Cat('Сима',3,'Мяукает')
d = Dog('Дик',5,'Гавкает')
b = Birds('Аргоша',2,'Чирикает')

for pet in [c,d,b]:
    print(pet.get_spec())