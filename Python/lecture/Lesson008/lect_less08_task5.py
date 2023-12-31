
# Если же мы хотим отказаться от символов экранирования в JSON файле, следует
# установить дополнительный параметр ensure_ascii в значение ложь.

import json

my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование","путешествия"],
    "age": 35,
    "children": [
        {
        "first_name": "Алиса",
        "age": 5
        },
        {
        "first_name": "Маруся",
        "age": 3
        }
    ]
}
direct = 'Python/lecture/Lesson008'
with open(f'{direct}/new_user.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f, ensure_ascii=False)