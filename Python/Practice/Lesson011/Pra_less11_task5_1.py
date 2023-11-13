# Задание №5
# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр
# прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.



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
        return 2*(self.l+self.h)
    
    def square(self):
        return self.l*self.h
    
    def __str__(self) -> str:
        return f'Высота прямоугольника = {self.l}, Длина прямоугольника = {self.h}'
    
    def __add__ (self, other):
        if isinstance(other,Rectangle):
            l = self.l + other.l
            h = self.h + other.h
            return Rectangle(l,h)
        raise TypeError
    
    def __sub__ (self, other):
        if isinstance(other,Rectangle):
            if(self.l > other.l or self.h > other.h):
                l = self.l - other.l
                h = self.h - other.h
                return Rectangle(l,h)
        raise TypeError

p1 = Rectangle(5,6)
p2 = Rectangle(10,8)

p3 = p2 - p1

print(p3)