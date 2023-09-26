import os
from pathlib import Path

path_folder = 'Python/lecture' # Путь к папки
name_folder = path_folder+'/Lesson008' #Название файла

os.mkdir(name_folder)

for num in range(1,50+1):
    name = f'{name_folder}/lect_less{name_folder[-2]+name_folder[-1]}_task{num}.py'
    
    f = open(name, 'x', encoding='utf-8')
    f.close()
