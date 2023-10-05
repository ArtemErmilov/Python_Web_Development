import os
from pathlib import Path

path_folder = 'Python/lecture' # Путь к папки
name_folder = path_folder+'/Lesson010' #Название файла
try:
    os.mkdir(name_folder)
except:
    pass

for num in range(1,30):
    try:
        name = f'{name_folder}/lec_less{name_folder[-2]+name_folder[-1]}_task{num}.py'
        
        f = open(name, 'x', encoding='utf-8')
        f.close()
    except:
        continue