# Задание №2
# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random

vowel_letters = 'ауоеёиэыяю'
consonants_letters = 'бвгджзйклмнпрстфхцчшщъь'
letters = vowel_letters+consonants_letters


def name(min_len_name:int=4,max_len_name:int = 7)->str:    
    
    lat = ''
    name =''
    len_num =  random.randint(min_len_name,max_len_name)
    max_num = len(letters)
    temp = True

    for count in range(len_num):
        i = random.randint(0,max_num)

        if (i<10):
            temp = False
        if (count==len_num-2 and temp):

            max_num = 10

        if (count==0):
            lat = letters[i].upper()
        else:
            lat = letters[i]
        name += lat


    return name

def generate_name (min_len_name:int=4,max_len_name:int = 7):
    size = random.randint(min_len_name,max_len_name+1)
    name = random.sample(letters,size-1)
    name.append(random.choice(vowel_letters))
    random.shuffle(name)
    name = ''.join(name).title()
    return name

def random_name (min_len_name:int=4,max_len_name:int = 7):
    vowel_letters_set = set(vowel_letters)
    consonants_letters_set = set (consonants_letters)

    len_name = random.randint(min_len_name,max_len_name+1)
    name = ''

    for i in range(len_name):
        name += random.choice(list(vowel_letters_set)) if i%2 else random.choice(list(consonants_letters_set))
    
    return name.title()




directory = 'Python/Practice/Lesson007'
name_file = 'Pra_Less7_task2_data.txt'
dir_name_fi = f'{directory}/{name_file}'  
name_new = name()
print(generate_name())
print(random_name())
print(name_new)
with open(dir_name_fi, 'a', encoding='utf-8') as f:
   f.write(f'generate_name = {generate_name()}\nrandom_name = {random_name()}\nname = {name_new}\n')