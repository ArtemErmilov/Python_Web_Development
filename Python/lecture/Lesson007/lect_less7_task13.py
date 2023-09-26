fil = r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Python Web Development\Python\lecture\Lesson007'
name_text_data = 'text_data.txt'
file_text_data = f'{fil}\{name_text_data}'

SIZE = 100
with open(file_text_data, 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE):
        print(res)