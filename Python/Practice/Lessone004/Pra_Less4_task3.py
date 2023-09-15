# Задание №3

# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до
#  наибольшего включительно.

def set_unicode (data:str):
    str_list = data.split()
    number_list = []
    min_nu = min(int(str_list [0]),int(str_list [1]))
    max_nu = max(int(str_list [0]),int(str_list [1]))
    for data in range(min_nu,max_nu+1):
        number_list.append(int(data))
    
    dict_list = {}
    for da in  sorted(number_list):
         dict_list[chr(da)] = da
    
    return dict_list 


def set_unicode_new (data:str) -> dict:# Задача с практики
    number_list = [int(data) for data in data.split()]
    dct_list = {chr(i):i for i in range(min(number_list),max(number_list)+1)}
    return dct_list

def set_unicode_map (data:str) -> dict:# Задача с практики
    number_list = list(map(int,data.split()))
    dct_list = {chr(i):i for i in range(min(number_list),max(number_list)+1)}
    return dct_list

input_num ='200 150'

print(set_unicode_map(input_num))

