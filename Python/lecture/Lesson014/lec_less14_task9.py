import doctest
import unittest
import lec_less14_task8

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(lec_less14_task8))
    tests.addTests(doctest.DocFileSuite('prime.md'))
    return tests

if __name__ == '__main__':
    unittest.main(verbosity=2)