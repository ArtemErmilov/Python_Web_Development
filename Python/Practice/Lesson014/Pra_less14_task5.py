# Задание №5
# 📌 На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# 📌 Напишите 3-7 тестов unittest для данного класса.

from Pra_less12_task4 import Rectangle

import unittest

class TestUnitCheck(unittest.TestCase):

    def setUp(self):
        self.first = Rectangle(2,3)
        self.second = Rectangle(4,5)
        self.another_first = Rectangle(2,3)
    
    def test_eq(self):
        self.assertTrue(self.first != self.another_first)
    
    def test_is(self):
        self.assertFalse(self.first is self.another_first)
    
    def test_not_eq(self):
        self.assertFalse(self.first == self.second)

    def test_sum(self):
        self.assertEqual(self.first + self.second, Rectangle(6,8))
    
    def test_exist(self):
        self.assertRaises(ValueError, Rectangle,(0,3))

if __name__ == '__main__':
    unittest.main(verbosity=2)
