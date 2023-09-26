import os
from pathlib import Path

print(os.listdir()) # Показывает какие директории и файлы находятся в корневой папке 

p = Path(Path().cwd())
for obj in p.iterdir(): # Вывод папок и файлов на печать
    print(obj)