class Person:
    max_up = 3
    def __init__(self): # Атрибут уровня экземпляра, класс к данным атрибутам уровня не имеет.
        self.level = 1
        self.health = 100
        print(f'{id(self) = }')

p1 = Person()
print(f'{id(p1) = }')
p2 = Person()
print(f'{id(p2) = }')