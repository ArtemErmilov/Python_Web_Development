# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from task5 import generator_multi_file

directory_new = 'Python/Practice/Lesson007'
new_directory_new = 'Pra_Less7_task5'

list_data_dict = {'txt':10,'pdf':5,'py':10,'doc':5}

generator_multi_file(directory_new, new_directory_new,list_data_dict )