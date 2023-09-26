# Возврат значения

def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 *a)
    if d == 0:
        return -b / (2 * a)
    return None

print(quadratic_equations(2, -3, -9))


# Неявный return
# Иногда функции не возвращают значения. Точнее нет явного возврата. В этом
# случае Python “мысленно” дописывает в качестве последней строки функции return
# None. Немного изменим прошлый пример и посмотрим на новый результат.

def no_return(data: list[int]):
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data = }') # Для демонстрации работы, но не для привычки принтить из функции
    
my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = no_return(my_list)
print(f'{my_list = }\t{new_list = }')