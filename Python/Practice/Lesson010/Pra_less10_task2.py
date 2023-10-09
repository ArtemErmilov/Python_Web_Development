# Задание №2
# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр
# и площадь.
# 📌 Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:

    def __init__(self,l:float,h = None):
        self.l = l
        self.h = h if h else l
       
        
    def perimeter(self):
        return 2*(self.l+self.h)
    
    def square(self):
        return self.l*self.h

p = Rectangle(5,6)

print(p.perimeter())
print(p.square())