# Задание №1
# 📌 Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.

def input_number(text:str):

    while True:
        try:
            data = input(text)
            data = float(data)
            return int(data) if int(data) == data else data
        
        except ValueError as e:
            print('Введённое значение не является числом. Введите число заново!')
            continue
       

print(input_number('Введите число: '))