import unittest
from utils import utils


class TestUtils(unittest.TestCase):

    def test_reversed(self):
        self.assertEqual(utils.reversed(12345), 54321)
        self.assertIsNone(utils.reversed("12345"))
        self.assertIsNone(utils.reversed(12.5))

    def test_formatter(self):
        self.assertEqual(utils.formatter(10), ("0b1010", "0o12"))
        self.assertIsNone(utils.formatter("10"))
        self.assertIsNone(utils.formatter(10.5))


if __name__ == "__main__":
    unittest.main()