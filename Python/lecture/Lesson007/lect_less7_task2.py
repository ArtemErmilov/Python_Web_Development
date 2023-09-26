# Чтобы избежать проблем при работе с файлами рекомендуется при открытии
# указывать как минимум три параметра: название файла, режим и кодировку.
fil = r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Python Web Development\Python\lecture\Lesson007\text_data.txt'
f = open(fil, 'r', encoding='utf-8')
print(f)
print(list(f))