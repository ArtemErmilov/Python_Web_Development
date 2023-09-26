# ● Функция next
# Функция next имеет формат next(iterator[, default]). На вход функция принимает
# итератор, который вернула функция iter. Каждый вызов функции возвращает
# очередной элемент итератора.

# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter)) # StopIteration


data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))