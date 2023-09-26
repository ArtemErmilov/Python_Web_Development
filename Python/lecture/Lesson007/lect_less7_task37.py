# Копирование файла
import os
from pathlib import Path

os.replace(r'Python\lecture\Lesson007\newest_file.py', os.path.join(os.getcwd(), r'Python\lecture\Lesson007\dir', r'Python\lecture\Lesson007\new_name.py')) # Копирование файла с изменением имени

old_file = Path(r'Python\lecture\Lesson007\new_name.py')
new_file = old_file.replace(Path.cwd() / r'Python\lecture\Lesson007\new_os_dir' / old_file)