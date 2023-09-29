

import json
my_dict = {
"first_name": "Джон",
"last_name": "Смит",
"hobbies": ["кузнечное дело", "программирование",
"путешествия"],
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
dict_to_json_text = json.dumps(my_dict) # Выведите текст русский текст в виде байт (символов экранирования)
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

dict_to_json_text = json.dumps(my_dict, ensure_ascii=False) # Выведет в нормальном виде русский текст.
print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')