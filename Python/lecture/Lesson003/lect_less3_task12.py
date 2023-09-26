# Срезы
#list[start:stop:step]
# Используя квадратные скобки можно делать частичные копии списка - срезы.
# - Срезы. Start указывает на первый индекс. 
# Stop указывает на последний индекс. step — шаг движения от star до stop. 

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list[2:7:2])
print(my_list[:7:2])
print(my_list[2::2])
print(my_list[2:7:])
print(my_list[8:3:-1])
print(my_list[3::])
print(my_list[:7:])