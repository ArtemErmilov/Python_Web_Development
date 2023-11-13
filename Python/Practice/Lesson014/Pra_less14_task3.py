# Задание №3
# 📌 Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import unittest
from Pra_less14_task2 import clear_text

class TestMyUnit(unittest.TestCase):

    def setUp(self):
        self.correct = 'text'
        self.first = 'TexT'
        self.second = 'Te..xt'
        self.third = 'Teфывxt'
        self.forth = 'Te..ЯЯ..xT'
    
    def test1(self):
        self.assertEqual(self.correct,clear_text(self.first))
    
    def test2(self):
        self.assertTrue(self.correct == clear_text(self.second))
    
    def test3(self):
        self.assertFalse(self.correct is clear_text(self.third))
    
    def test4(self):
        self.assertRaises(ValueError,clear_text,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
    
