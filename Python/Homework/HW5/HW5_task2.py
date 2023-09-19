# Задача 2

# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


file = r"C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Python Web Development\Python\Practice\Lessone002\Семинар 2. Простые типы данных.pdf"



def link_data(data_file) ->tuple:
    *data_file,extension = file.split('.')
    data_file = '.'.join(data_file)
    *path_file, file_name = data_file.split('\\')
    path_file = '\\'.join(path_file)

    return (path_file,file_name,extension,)

   

print(link_data(file))