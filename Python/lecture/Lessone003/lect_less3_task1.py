# Создание списков и добавление к ним данных
list_1 = list()
list_2 = list((3.14, True, "Hello world!"))
list_3 = []
list_4 = [3.14, True, "Hello world!"]

# Обращение к данным списка по индексу

my_list = [2, 4, 6, 8, 10, 12]
print(my_list[0])
#print(my_list[6]) # IndexError: list index out of range
print(my_list[-1])
#print(my_list[-10]) # IndexError: list index out of range