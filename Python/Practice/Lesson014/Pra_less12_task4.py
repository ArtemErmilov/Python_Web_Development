# Задание №4
# 📌 Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# 📌 Используйте декораторы свойств.


class Value:

    def __init__(self, min_value:int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self,owner,name):
        self.param_name = '_' + name
    
    def __get__(self,instance,owner):
        return getattr(instance,self.param_name)
    
    def __set__(self, instance,value):
        setattr(instance, self.param_name, self._validate(value))

    def _validate(self, value: int ):
        if not(self.min_value < value < self.max_value):
            raise ValueError
        return value

class Rectangle:
    l = Value(1,100)
    h = Value(1,100)
    """
    Класс прямоугольника
    """
    
    #__slots__ = ['l','h']

    def __init__(self,l:float,h = None):
        self.l = l
        self.h = h if h else l
              
               
        
    def perimeter(self):
        self.perimeter = 2*(self.l+self.h)
        return self.perimeter
    
    def square(self):
        self.square = self.l*self.h
        return self.square
    
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
    
    def __eq__(self, other):
        return self.l == other.l and self.h == other.h
    
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