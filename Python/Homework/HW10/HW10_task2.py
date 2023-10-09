# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

# ДЗ №4 Задача 1
# Напишите функцию для транспонирования матрицы

class MyMatrix:

    def __init__(self, matrix:list):

        self.matrix = matrix
    
    def get_matrix(self):
        return self.matrix

    def get_matrix_transp(self):
        x_len = len(self.matrix[0])
        y_len = len(self.matrix)
        self.matrix_transp = []
        for i in range(x_len):
            new_list = []
            for j in range (y_len):
                new_list.append(self.matrix[j][i])
            self.matrix_transp.append(new_list)
        return self.matrix_transp


def print_matrix(matrix_list:list):
    x_len = len(matrix_list[0])
    y_len = len(matrix_list)
    print()
        
    for i in range (y_len):
        text = ''
        for j in range (x_len):
            text = text + str(matrix_list[i][j])+'\t'
        print(f'{text}\n')
            

    
    
if __name__ == '__main__':

    

    m = MyMatrix([[1,2],[3,4],[5,6],[7,8]])

    print_matrix(m.get_matrix())
    print('Транспонированная матрица:')
    print_matrix(m.get_matrix_transp())

