# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from task6 import generator_multi_file_direc

direct = 'Python/Practice/Lesson007'
new_direct= 'Pra_Less7_task6'

list_data_dict = {'txt':10,'pdf':5,'py':10,'doc':5}

generator_multi_file_direc(direct, new_direct,list_data_dict )