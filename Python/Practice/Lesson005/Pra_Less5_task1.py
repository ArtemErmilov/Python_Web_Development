# Задание №1

# Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.

# Сформируйте словарь, где:
#       второе и третье число являются ключами.
#       первое число является значением для первого ключа.
#       четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа.


number = '1/2/3/4/5/6/7/8/9/10'

data1, key1, key2, *data2 = number.split('/')


dict_list = {key1:data1,key2:data2}


print(dict_list)