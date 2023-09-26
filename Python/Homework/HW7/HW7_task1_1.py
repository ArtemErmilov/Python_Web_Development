# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from task1 import generator_multi_file_direc,  sorting_files

direct = 'Python/Homework/HW7'
new_direct= 'HW7_task1'

list_data_dict = {'txt':10,'pdf':5,'py':10,'doc':5,'docx':3, 'md':3,'bmp':2,'jpeg':3,'gif':4,'mp3':3,'mp4':3,'wma':2,'mpeg':3,'md':5}

#generator_multi_file_direc(direct, new_direct,list_data_dict ) #Добавление новых файлов.

sorting_files(f'{direct}/{new_direct}')