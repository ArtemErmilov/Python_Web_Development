import unittest

class TestCaseName(unittest.TestCase): # В название класса должно быть слово Test

    def test_method(self): # В название метода должно быть слово test
        self.assertEqual(2 * 2, 5, msg='Видимо и в этой вселенной не работает :-(')


if __name__ == '__main__':
    unittest.main()