#Прочие необязательные параметры функции open
fil = r'C:\Users\SBB2-Ермилов Артём\YandexDisk-artyomermiloff\GeegBrains\Programming\Technological specialization\Python Web Development\Python\lecture\Lesson007'
name_f = f'{fil}\_bin_data'
f = open(name_f, 'wb', buffering=64)
f.write(b'X' * 1200)
f.close()