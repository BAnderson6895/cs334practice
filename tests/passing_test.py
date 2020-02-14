import unittest

class Test(unittest.TestCase):

    def test_pass(self):
        result = 0
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
