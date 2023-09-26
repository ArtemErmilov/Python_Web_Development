fil = r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Python Web Development\Python\lecture\Lesson007'
name_f = f'{fil}\_data.txt'

f = open(name_f, 'wb')
f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
f.close()

f = open(name_f, 'r', encoding='utf-8')
print(list(f)) # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xec in position 14: invalid continuation byte


f.close()
f = open(name_f, 'r', encoding='utf-8', errors='replace')
print(list(f))
f.close()