# Задание №2
# 📌 Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

from string import ascii_lowercase

import doctest

def clear_text(text:str):
    """
    >>> clear_text('aqwert') == 'aqwert'
    True
    >>> clear_text('aqweRT') == 'aqwert'
    True
    >>> clear_text('aqwe,.') == 'aqwe'
    True
    >>> clear_text('aqweфыва') == 'aqwe'
    True
    >>> clear_text('aqwert aqweRT aqwe,. aqweфыва') == 'aqwert aqwert aqwe aqwe'
    True
    """
    result = ''
    if text is not None:
        for i in text.lower():
            if i in ascii_lowercase + ' ':
                result +=i
        return result
    raise ValueError('Incorrect text')

if __name__ == '__main__':
    doctest.testmod(verbose=True)