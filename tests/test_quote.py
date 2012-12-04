# coding: utf-8
import unittest
from quote import Quote

class TestBlog(unittest.TestCase):
    def test_shorten_msg(self):
        quote = Quote()
        s = '''
        1234567890123456789012345678901234567890
        1234567890123456789012345678901234567890
        1234567890123456789012345678901234567890
        1234567890123456789012345678901234567890
        '''
        ss = quote.shorten_msg(s)
        self.assertEquals(len(ss) + 1 + 20, 140)

if __name__ == '__main__':
    unittest.main()
