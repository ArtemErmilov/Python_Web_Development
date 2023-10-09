# Задание №1

# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

from cmath import pi


class Circle:
    def __init__(self,r:float):
        self.r = self.check_radius(r)
    def check_radius(self,r):
        if (r>0):
            return r
        raise ValueError
    def perimeter(self):
        return 2*self.r*pi
    def square(self):
        return pi*self.r**2

c = Circle(8)

print(c.perimeter())
print(c.square())