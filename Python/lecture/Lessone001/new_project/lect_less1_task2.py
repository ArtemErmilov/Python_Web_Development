
pwd = 'text'

res = input('Введите пароль: ')

if res == pwd :
    print ('Доступ разрешён!')
    print('Но будьте осторожны!')
    my_math = int(input('2 + 2 = '))
    if 2 + 2 == my_math:
        print('Вы в нормальном мире')
    else:
        print('Но будьте осторожны')
else:
    print('Доступ запрещён!')
print('Работа завершена')