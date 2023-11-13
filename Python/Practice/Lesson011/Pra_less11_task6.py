# Задание №6
# 📌 Доработайте прошлую задачу.
# 📌 Добавьте сравнение прямоугольников по площади
# 📌 Должны работать все шесть операций сравнения

from functools import total_ordering

@total_ordering
class Rectangle:
    """
    Класс прямоугольника
    """

    def __init__(self,l:float,h = None):
        self.l = l
        self.h = h if h else l
        if (l<=0 or h<=0):
            raise TypeError('Значение меньше или равно 0')
        self.perimeter = self.perimeter()
        self.square = self.square()
        
        
    def perimeter(self):
        """
        Вычисление периметра треугольника.
        """
        return 2*(self.l+self.h)
    
    def square(self):
        """
        Вычисление площади треугольника.
        """
        return self.l*self.h
    
    def __str__(self) -> str:
        return f'Высота прямоугольника = {self.l}, Длина прямоугольника = {self.h}'
    
    def __add__ (self, other):
        """
        Метод сложения треугольников по его сторонам.
        """
        if isinstance(other,Rectangle):
            l = self.l + other.l
            h = self.h + other.h
            return Rectangle(l,h)
        raise TypeError
    
    def __sub__ (self, other):
        """
        Метод вычитания треугольников по его сторонам.
        """
        if isinstance(other,Rectangle):
            if(self.l > other.l or self.h > other.h):
                l = self.l - other.l
                h = self.h - other.h
                return Rectangle(l,h)
        raise TypeError
    
    def __eq__(self,other):
        """
        Метод сравнения двух экземпляров треугольников.
        """
        if isinstance(other,Rectangle):
            return self.square == other.square
        raise TypeError
    
    def __gt__(self,other):
        """
        Метод сравнения на больше двух экземпляров треугольников.
        """
        if isinstance(other,Rectangle):
            return self.square > other.square
        raise TypeError

    # def __le__ (self,other):
    #     if isinstance(other,Rectangle):
    #         return self.square >= other.square
    #     raise TypeError

    

p1 = Rectangle(5,6)
p2 = Rectangle(10,8)



print(p1 == p2)
print(p1 > p2)
print(p1 < p2)
print(p1 >= p2)
print(p1 <= p2)
print(p1 != p2)