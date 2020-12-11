import unittest

from ..example import function


class TestExampleFunction(unittest.TestCase):

    def test_function(self):
        self.assertEqual(5, function(2, 3))


if __name__ == '__main__':
    unittest.main()
