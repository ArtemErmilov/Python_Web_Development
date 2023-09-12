# Работа со строками как с массивами

text = 'Hello world!' # работает ка срез
print(text[6])
print(text[3:7])

new_txt = text.replace('l', 'L', 2)
print(text, new_txt, sep='\n')