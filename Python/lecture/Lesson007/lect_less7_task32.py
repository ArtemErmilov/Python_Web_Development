import os
from pathlib import Path

file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt') # Возвращение строки
print()
print(f'{file_1 = }\n{file_1}')
print()

file_2 = Path().cwd() / 'dir' / 'new_file.txt' # Возвращение объекта
print(f'{file_2 = }\n{file_2}')
print()