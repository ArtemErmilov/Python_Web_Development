# Задание №5

# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря -загадка, значение -список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.


import random


def gen_puzzle():
    func_dict = {'Зимой и летом одним цветом.':['ёлка','ёлочка','ель'], 
                'Все меня любят, а как раздевать - слезы проливать':['лук','лучок','репчатый'],
                'Весит груша нельзя скушать': ['лампочка', 'лампа']}

    while func_dict:
        key = random.choice(list(func_dict))
        yield key, func_dict.pop(key)

def mystery (item: int = 3, count:int = 5):

    result = []
    puzzles = gen_puzzle()
    
    for _ in range(item):
        text_my,answer = next(puzzles)
        answer = list(map(lambda x: x.lower(),answer))
        for cou in range(1,count+1):           
            ans = str(input(f'{text_my} Ответ:')).lower()
            if (ans in answer):
                result.append(cou)
                break
        else:
            result.append(0)
    return result