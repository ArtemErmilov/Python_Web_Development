import os
from pathlib import Path

path_folder = 'Python/Practice' # Путь к папки
name_folder = path_folder+'/Lesson009' #Название файла
try:
    os.mkdir(name_folder)
except:
    pass

for num in range(1,6+1):
    try:
        name = f'{name_folder}/Pra_less{name_folder[-2]+name_folder[-1]}_task{num}.py'
        
        f = open(name, 'x', encoding='utf-8')
        f.close()
    except:
        continue