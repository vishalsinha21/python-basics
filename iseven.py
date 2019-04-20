
def isEven(num):
    return num%2 == 0

for i in range(1, 11):
    print('for i', i, 'isEven is', isEven(i))

import unittest

class TestIsEvenMethod(unittest.TestCase):
    def test_isEven1(self):
        self.assertEqual(isEven(5), False)

    def test_isEven2(self):
        self.assertEqual(isEven(10), True)

    def test_isEven3(self):
        with self.assertRaises(TypeError):
            isEven('hello')

unittest.main()
