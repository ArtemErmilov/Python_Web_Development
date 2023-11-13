# Задание №1

# 📌 Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.

from string import ascii_lowercase

def clear_text(text:str):
    result = ''
    for i in text.lower():
        if i in ascii_lowercase + ' ':
            result +=i
    return result

if __name__ == '__main__':
    text = 'dsdsоовывс ваkfk158овkdkлвлв влkkdfkалвTRлалfdlfvdk !#$dfdf%апап:ывыss'

    print(clear_text(text))