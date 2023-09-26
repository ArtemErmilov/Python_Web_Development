fil = r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Python Web Development\Python\lecture\Lesson007'
name_text_data = 'text_data.txt'
file_text_data = f'{fil}\{name_text_data}'
file_bin_data = f'{fil}\_bin_data'
file_data= f'{fil}\_data.txt'


with open(file_text_data, 'r+', encoding='utf-8') as f1, \
    open(file_bin_data, 'rb') as f2, \
    open(file_data, 'r', encoding='utf-8',errors='backslashreplace') as f3:

    print(list(f1))
    print(list(f2))
    print(list(f3))