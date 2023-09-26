fil = r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Python Web Development\Python\lecture\Lesson007'

for num in range(51,53):
    name = f'{fil}\lect_less7_task{num}.py'
    
    f = open(name, 'x', encoding='utf-8')
    f.close()
