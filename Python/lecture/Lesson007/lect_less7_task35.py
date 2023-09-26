import os

for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
    
    #dir_path - абсолютный путь до каталога
    #dir_name - dir_names — список с названиями всех каталогов, находящихся в dir_path
    #file_name - dir_names — список с названиями всех файлов, находящихся в dir_path