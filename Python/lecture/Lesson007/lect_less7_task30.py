import os
from pathlib import Path

# os.rmdir('dir') # OSError
# Path('some_dir').rmdir() # OSError

os.rmdir(r'Python\lecture\Lesson007\dir\other_dir\new_os_dir')
Path(r'Python\lecture\Lesson007\some_dir\dir\new_path_dir').rmdir()