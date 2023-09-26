color = input('Твой любимый цвет: ')
if color == 'красный':
    print('Любитель яркого')
elif color == 'зелёный':
    print('Ты не охотник?')
elif color == 'синий':
    print('Ха, классика!')
else:
    print('Тебя не понять')

color = input('Твой любимый цвет: ')
match color:
    case 'красный' | 'оранжевый':
        print('Любитель яркого')
    case 'зелёный':
        print('Ты не охотник?')
    case 'синий' | 'голубой':
        print('Ха, классика!')
    case _:
        print('Тебя не понять')