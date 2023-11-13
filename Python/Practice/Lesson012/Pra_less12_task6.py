# Задание №6
# 📌 Изменяем класс прямоугольника.
# 📌 Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.


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
    """
    Класс прямоугольника
    """
    
    #__slots__ = ['l','h']

    l = Value(10,100)
    h = Value(10,100)

    def __init__(self,l:float,h = None):
        self.l = l
        self.h = h if h else l
        # if (l<=0 or h<=0):
        #     raise TypeError('Значение меньше или равно 0')
        self.perimeter = self._perimeter()
        self.square = self._square()
        
        
    def _perimeter(self):
        return 2*(self.l+self.h)
    
    def _square(self):
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

