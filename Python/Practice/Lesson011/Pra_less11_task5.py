# Задание №5
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр
# прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.


import math


class MyTriangle:



    def __init__(self,side_a:int,side_b:int,side_c:int):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.triangle_status  = self.get_status()
        self.perimeter = self.get_perimeter()
        self.square = self.get_square()
        if (not self.triangle_status):
            raise ValueError ('Треугольника не существует')
        
    def get_status(self):

        sides = [self.side_a, self.side_b, self.side_c ]

        for side in sides:
            if side >= (sum(sides) - side):
                triangle_status = False
                break
        else:
            triangle_status = True
            
        return triangle_status

    def get_perimeter(self):
       
        return self.side_a + self.side_b + self.side_c
    
    def get_square(self):        
        
        p = float(self.perimeter)/2
        return math.sqrt(p*(p-float(self.side_a))*(p-float(self.side_b))*(p-float(self.side_c)))
    
    def __str__(self) -> str:
        return f'Сторона a = {self.side_a}, Сторона b = {self.side_b}, Сторона c = {self.side_c}'
    
    def __add__ (self, other):
        side_a = self.side_a + other.side_a
        side_b = self.side_b + other.side_b
        side_c = self.side_c + other.side_c
        return MyTriangle(side_a,side_b,side_c)
    
    def __sub__ (self, other):
        side_a = self.side_a - other.side_a
        side_b = self.side_b - other.side_b
        side_c = self.side_c - other.side_c
        return MyTriangle(side_a,side_b,side_c)

a = MyTriangle(5,6,7)
b = MyTriangle(10,10,10)

c = b - a

print(c)