# ДЗ №4 Задача 1
# Напишите функцию для транспонирования матрицы

def print_matrix(matrix_list:list):
    x_len = len(matrix_list[0])
    y_len = len(matrix_list)
    print()
    
    for i in range (y_len):
        text = ''
        for j in range (x_len):
            text = text + str(matrix_list[i][j])+'\t'
        print(f'{text}\n')
        

def matrix_transp(matrix_list:list):
    x_len = len(matrix_list[0])
    y_len = len(matrix_list)
    data_list = []
    for i in range(x_len):
        new_list = []
        for j in range (y_len):
            new_list.append(matrix_list[j][i])
        data_list.append(new_list)
    return data_list
    

matrix = [[1,2],[3,4],[5,6]]


print_matrix(matrix)
print('Транспонированная матрица:')
print_matrix(matrix_transp(matrix))

