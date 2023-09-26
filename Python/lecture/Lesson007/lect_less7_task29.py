import os
from pathlib import Path

os.makedirs(r'Python\lecture\Lesson007\dir\other_dir\new_os_dir')
Path(r'Python\lecture\Lesson007\some_dir\dir\new_path_dir').mkdir() # FileNotFoundError
Path(r'Python\lecture\Lesson007\some_dir\dir\new_path_dir').mkdir(parents=True)