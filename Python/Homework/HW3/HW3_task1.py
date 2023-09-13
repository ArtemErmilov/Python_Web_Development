# Задача 8 из практики
# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:

# ✔ Какие вещи взяли все три друга

# ✔ Какие вещи уникальны, есть только у одного друга

# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует

# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее 
# количество друзей.




tourist = { 'Вася' : ( 'Палатка' , 'Спички' , 'Нож'), 'Петя' : ( 'Палатка' , 'Удочка' , 'Спальник' ), 'Саша' : ( 'Спальник' , 'Спички' , 'Котелок'),}

text =  ' 1 - Введите имя друга и вещи, которые он возьмёт с собой в поход.\n'\
        ' 2 - Какие вещи взяли все друзья в поход\n'\
        ' 3 - Введите имя друга и увидите, какие у него есть уникальные вещи.\n'\
        ' 4 - Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует.\n'


while True:
    
    print(text)
    a = int(input('Введите значения от 1 до 4. Для выхода ведите любой символ и, или Enter. => '))
    if a == 1:
        name = str(input('Введите имя туриста: '))

        stuff = str(input('Введите вещи, которые с собой возьмёт турист через пробел: '))
        stuff_tuple = tuple(stuff.split())
        tourist[name] = stuff_tuple
        continue    
    elif (a == 2 ):
        vel = set({})
        for value in tourist.values():
            new_vel = set(value)
            vel = vel.union(new_vel)
        print (f'Вещи, которые взяли все туристы {vel}')
        
        b = str(input('Для продолжения нажмите Enter'))
        continue
    
    elif (a == 3 ):
        name = str(input('Введите имя: '))
        v = set(tourist[name])
        for value in tourist.keys():
            if (name != value):
                new_vel = set(tourist[value])
                v = v - new_vel
        print (f'Уникальная вещь {str(v)[2:-2:]} у {name}')
        b = str(input('Для продолжения нажмите Enter'))
        continue    
    elif (a == 4 ):
        vel = set({})
        for value in tourist.values():
            new_vel = set(value)
            vel = vel.union(new_vel)

        for data in vel:
            print(f'Вещь : {data}')
            for name in tourist.keys():
                if not(tourist[name].count(data)):
                    print(f'{data} нет у {name}')
        b = str(input('Для продолжения нажмите Enter'))       
        continue

    else:
        break