size = 64
with open(r'Python\lecture\Lesson007\new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))