# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

# Задача 1

# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
# стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
# двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
# с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

import math


class MyTriangle:

    def __init__(self,side_a:int,side_b:int,side_c:int):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.triangle_status = self.get_status()
        self.perimeter = self.get_perimeter()
        self.square = self.get_square()

    def get_status(self):

        sides = [a,b,c]
        for side in sides:
            if side >= (sum(sides) - side):
                triangle_status = 'Треугольника не существует'
                break
        else:
            t = {a,b,c}
            if len(t) == 1:
                triangle_status = 'Треугольник равносторонний'
            elif len(t) == 2:
                triangle_status = 'Треугольник равнобедренный'
            else:
                triangle_status = 'Треугольник разносторонний'
            
        return triangle_status

    def get_perimeter(self):
        if (self.triangle_status == 'Треугольника не существует'):
            return
        else:
            return self.side_a + self.side_b + self.side_c
    
    def get_square(self):
        if (self.triangle_status == 'Треугольника не существует'):
            return
        else:
            p = float(self.perimeter)/2
            return math.sqrt(p*(p-float(self.side_a))*(p-float(self.side_b))*(p-float(self.side_c)))

if __name__ == '__main__':

    a = int(input('Введите длину первой стороны треугольника: '))
    b = int(input('Введите длину второй стороны треугольника: '))
    c = int(input('Введите длину третей стороны треугольника: '))

    t = MyTriangle(a,b,c)

    print(t.get_status())
    print(t.perimeter)
    print(t.get_square())
