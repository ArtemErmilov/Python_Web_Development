# Задание №4

# 📌 Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# 📌 Дополните id до 10 цифр незначащими нулями.
# 📌 В именах первую букву сделайте прописной.
# 📌 Добавьте поле хеш на основе имени и идентификатора.
# 📌 Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# 📌 Имя исходного и конечного файлов передавайте как аргументы
# функции.

from functions_Less8 import file_creation_csv_json

directory =  'Python/Practice/Lesson008'
new_directory = 'Pra_Less8_task4'

name_file_csv = 'Pra_Less8_task3_csv'
name_file_json = 'Pra_Less8_task4_json'


file_creation_csv_json(directory, new_directory,name_file_csv=name_file_csv,name_file_json=name_file_json)