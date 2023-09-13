# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

import random 

num_list = []

for _ in range(10):
    num_list.append(random.randint(1,10))

print(num_list)

new_list = []

for num in set(num_list):
    if (num_list.count(num) >= 2):
        new_list.append(num)


print(new_list)
