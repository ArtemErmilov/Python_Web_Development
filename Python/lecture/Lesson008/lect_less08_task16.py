import pickle

direct = 'Python/lecture/Lesson008'
def func(a, b, c):
    return a + b + c
my_dict = {
    "numbers": [42, 4.1415, 7+3j],
    "functions": (func, sum, max),
    "others": {True, False, 'Hello world!'},
    }

with open(f'{direct}/my_dict.pickle', 'wb') as f:
    pickle.dump(my_dict, f)