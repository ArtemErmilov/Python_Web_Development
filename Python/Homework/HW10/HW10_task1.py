# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

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

class Factory():

    def __init__(self, tips_animals:str, name:str, agy:int, spec:str):
        
        self.tips_animals = tips_animals.lower()
        self.name = name
        self.agy = agy
        self.spec = spec

    def get_class(self):        
        if (self.tips_animals=='dog'):
            return Dog(self.name,self.agy,self.spec)
        elif(self.tips_animals=='cat'):
            return Cat(self.name,self.agy,self.spec)
        elif(self.tips_animals=='birds'):
            return Birds(self.name,self.agy,self.spec)


if __name__ == '__main__':

    temp = Factory('dog','Шарик', 5,'гав')

    temp = temp.get_class()

    print(type(temp))
    print(f'Кличка {temp.name}, возраст: {temp.agy}, особенности: {temp.spec}')