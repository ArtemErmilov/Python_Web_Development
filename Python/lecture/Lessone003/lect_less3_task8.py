# Метод remove
# Метод remove принимает на вход объект, производит его поиск в списке и удаляет в
# случае нахождения.

my_list = [2, 4, 6, 8, 10, 12, 6]
my_list.remove(6)
print(my_list)
my_list.remove(3) # ValueError: list.remove(x): x not in list
print(my_list)