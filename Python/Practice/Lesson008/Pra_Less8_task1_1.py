# Задание №1

# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

from functions_Less8 import wer_file_number, wr_file_name, reading_file, file_creation_json

directory =  'Python/Practice/Lesson008'
new_directory = 'Pra_Less8_task1'
name_file_number = 'Pra_Less8_task1_number.txt'
name_file_name = 'Pra_Less8_task1_name.txt'
name_file_new = 'Pra_Less8_task1_new.txt'
name_file_jsone = 'Pra_Less8_task1_json.json'

wer_file_number(directory,new_directory,name_file=name_file_number)
wr_file_name(directory,new_directory,file_name=name_file_name)
reading_file(directory,new_directory,file_num= name_file_number, file_name=name_file_name,new_name_file=name_file_new)

file_creation_json(directory,new_directory,original_file_name=name_file_new,new_json_file_name=name_file_jsone)