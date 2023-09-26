#Переименование файлов

import os
from pathlib import Path

f = open('Python/lecture/Lesson007/old_name.py', 'x', encoding='utf-8')
f.close()

f = open('Python/lecture/Lesson007/old_file.py', 'x', encoding='utf-8')
f.close()


os.rename('Python/lecture/Lesson007/old_name.py', 'Python/lecture/Lesson007/new_name.py')

p = Path('Python/lecture/Lesson007/old_file.py')
p.rename('Python/lecture/Lesson007/new_file.py')

Path('Python/lecture/Lesson007/new_file.py').rename('Python/lecture/Lesson007/newest_file.py')