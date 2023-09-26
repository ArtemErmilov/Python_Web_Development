# Для изменения текущего каталога можно воспользоваться функцией os.chdir.
import os
from pathlib import Path
print(os.getcwd())
print(Path.cwd())
os.chdir('../..')
print(os.getcwd())
print(Path.cwd())