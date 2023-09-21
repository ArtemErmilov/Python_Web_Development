# Задание №7
# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.


import random

def companies_cash(comp_dict : dict) -> bool:
    for data in comp_dict.values():
        if(sum(data)<0):
            return False  
    return True

def companies_cash_new(comp_dict : dict) -> bool: # C урока
    for i in comp_dict:
        comp_dict[i]= sum (comp_dict[i])
    print(comp_dict)

    return all(map(lambda x: x > 0, comp_dict.values()))


name_copan = ['adidas','hike','rybok', 'BMW']
companies = {name : [random.randint(-10000,10000) for _ in range(random.randint(3,10))] for name in name_copan}

print(companies)

print(companies_cash_new(companies))