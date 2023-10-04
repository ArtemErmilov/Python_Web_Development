from functools import wraps
import json
import os
from typing import Callable


def dec_wr_json (func:Callable, *,diretc:str = 'Python\Homework\HW9',\
                name_new_direct:str = 'HW9_task1', name_file:str = 'HW9_task1_json.json'):
    @wraps(func)
    def wrapper(*args,**kwargs):
        nonlocal diretc,name_new_direct,name_file
       
        full_direct = os.path.join(diretc,name_new_direct)
        full_name = os.path.join(full_direct, name_file)
        data = func(*args,**kwargs)
               
        with open (full_name,'w', encoding='utf-8') as f_json:
            json.dump(data,f_json,indent=4, separators=(',', ':'),sort_keys=True)

    return wrapper