import os
from pathlib import Path
os.remove('Python/lecture/Lesson007/one_more_dir/one.txt')
Path('Python/lecture/Lesson007/one_more_dir/one_more.txt').unlink()