fil = r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Python Web Development\Python\lecture\Lesson007'
name_text_data = 'new_data.txt'
file_new_data = f'{fil}\{name_text_data}'
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open(file_new_data, 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))