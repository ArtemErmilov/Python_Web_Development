#Копирование файлов 

import shutil

f = open('Python/lecture/Lesson007/one.txt', 'x', encoding='utf-8')
f.close()

f = open('Python/lecture/Lesson007/two.txt', 'x', encoding='utf-8')
f.close()

shutil.copy('Python/lecture/Lesson007/one.txt', 'Python/lecture/Lesson007/dir') # Копирует фаил, но игнорирует метаданные
shutil.copy2('Python/lecture/Lesson007/two.txt', 'Python/lecture/Lesson007/dir') # Копирует фаил, не игнорирует метаданные