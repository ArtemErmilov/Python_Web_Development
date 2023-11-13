# Задание №4
# 📌 Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# 📌 Используйте декораторы свойств.


class Rectangle:
    """
    Класс прямоугольника
    """
    
    __slots__ = ['l','h']

    def __init__(self,l:float,h = None):
        self.l = l
        self.h = h if h else l
        # if (l<=0 or h<=0):
        #     raise TypeError('Значение меньше или равно 0')
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
    
    @property
    def width(self):
        return self.l
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError('Так нельзя')
        self.l = value

    @property
    def hight(self):
        return self.h
    
    @hight.setter
    def hight(self, value):
        if value <= 0:
            raise ValueError('Так нельзя')
        self.h = value
        
if __name__ == '__main__':
    p1 = Rectangle(5,6)
    p2 = Rectangle(10,8)

    p3 = p2 - p1

    print(p1)