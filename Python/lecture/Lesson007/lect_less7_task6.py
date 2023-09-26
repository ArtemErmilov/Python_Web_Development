fil = r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Python Web Development\Python\lecture\Lesson007'
name = 'text_data.txt'
file = f'{fil}\{name}'

with open(file, 'r+', encoding='utf-8') as f:
    print(list(f))
print(f.write('Пока')) # ValueError: I/O operation on closed file.