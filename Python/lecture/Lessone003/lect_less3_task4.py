# Метод pop
# Метод pop позволяет удалить элемент списка. Удаляемый элемент возвращается
# как результат работы метода.
my_list = [2, 4, 6, 8, 10, 12]
spam = my_list.pop() # Если нет значения индекса, то будет удалён последний элемент.
print(spam, my_list)
eggs = my_list.pop(1)
print(eggs, my_list)
err = my_list.pop(10) # IndexError: pop index out of range