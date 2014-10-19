#Purpose: Unit tests for Lempel-Ziv-Welch algorithm
from lzw import compress
import unittest

class TestLZW(unittest.TestCase):

    def test_typical_cases(self):

        string = "TOBEORNOTTOBEORTOBEORNOT"
        result = compress(string)
        self.assertSequenceEqual(result, [84, 79, 66, 69, 79, 82, 78, 79, 84, 256, 258, 260, 265, 259, 261, 263])

        string = "^WED^WE^WEE^WEB^WET"
        result = compress(string)
        self.assertSequenceEqual(result, [94, 87, 69, 68, 256, 69, 260, 261, 257, 66, 260, 84])

        string = "thisisthe"
        result = compress(string)
        self.assertSequenceEqual(result, [116, 104, 105, 115, 258, 256, 101])

if __name__=='__main__':
    unittest.main()
