# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

import numpy as np
from functools import total_ordering


#@total_ordering
class MyMatrix:
    """
    Класс матрица. Математические операции проводимые с матрицей.

    Атрибуты:
    matrix (list): матрица с числовыми значениями.


    Dunder методы:
    __new__(cls, value, author): создает новый объект класса.
    __str__(): возвращает строковое представление объекта класса.
    __repr__(): возвращает строковое представление объекта класса для отладки.
    __add__(): сложение двух матриц

    """

    def __new__ (cls,matrix:list):
        instance = super().__new__(cls)
        instance.matrix = matrix
        return instance
    
    def __str__ (self):
        matrix_p = '\n'
        for i in range(len(self.matrix)):
            temp = ''
            for j in range(len(self.matrix[i])):
                temp += f'{self.matrix[i][j]}\t'
            matrix_p += temp + '\n\n'
        return matrix_p
    
    def __add__ (self, other):
        """
        Сложение двух матриц.
        """
        
        if isinstance(other,MyMatrix) and len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            matrix = []
            for i in range(len(self.matrix)):
                temp = []
                for j in range(len(self.matrix[i])):
                    temp.append(self.matrix[i][j] + other.matrix[i][j])
                matrix.append(temp)

            return MyMatrix(matrix)
        raise ValueError

    def __eq__  (self, other):
        """
        Сравнение двух матриц. Равно.
        """    
        if isinstance(other,MyMatrix) and len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            matrix = []
            for i in range(len(self.matrix)):
                temp = []
                for j in range(len(self.matrix[i])):
                    temp.append(self.matrix[i][j] == other.matrix[i][j])
                matrix.append(temp)

            return MyMatrix(matrix)
        raise ValueError
    
    def __gt__  (self, other):
        """
        Сравнение двух матриц. Больше.
        """    
        if isinstance(other,MyMatrix) and len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            matrix = []
            for i in range(len(self.matrix)):
                temp = []
                for j in range(len(self.matrix[i])):
                    temp.append(self.matrix[i][j] > other.matrix[i][j])
                matrix.append(temp)

            return MyMatrix(matrix)
        raise ValueError

    def __le__  (self, other):
            """
            Сравнение двух матриц. Больше или равно.
            """    
            if isinstance(other,MyMatrix) and len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
                matrix = []
                for i in range(len(self.matrix)):
                    temp = []
                    for j in range(len(self.matrix[i])):
                        temp.append(self.matrix[i][j] >= other.matrix[i][j])
                    matrix.append(temp)

                return MyMatrix(matrix)
            raise ValueError
    
    def __mul__  (self, other):
        matrix = []
        if (isinstance(other,int)) and len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            matrix =self.matrix
            return matrix

        elif (isinstance(other,MyMatrix)) and len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            for i in range(len(self.matrix)):
                    temp = []
                    for j in range(len(self.matrix[i])):
                        temp.append(self.matrix[i][j] * other.matrix[i][j])
                    matrix.append(temp)

            return MyMatrix(matrix)

        else:
            raise ValueError

# matrix1 = np.array([ [3, 5], [8, 7] ])
# matrix2 = np.array([ [5, 3], [1, 10] ])
# total = matrix1 + matrix2
# print(total)
# print(np.linalg.det(total))

m_1 = MyMatrix([ [8, 5, 6], [8, 7, 8] ])
m_2 = MyMatrix([ [8, 5, 8], [1, 10, 11] ])

print(m_1)
print(m_2)
print(m_1 + m_2)
print(m_1 == m_2)
print(m_1 >= m_2)
print(m_1 * 5)