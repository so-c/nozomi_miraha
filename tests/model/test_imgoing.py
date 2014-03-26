# coding: utf-8
import unittest
from model.imgoing import ImGoing

class TestImGoing(unittest.TestCase):
    def test_isImGoing(self):
        sut = ImGoing()

        actual = sut.isimgoing(u'いってきます')
        self.assertTrue(actual)
        
        actual = sut.isimgoing(u'いってきまーす')
        self.assertTrue(actual)
        
        actual = sut.isimgoing(u'いってきまーっす')
        self.assertTrue(actual)
        
        actual = sut.isimgoing(u'いってきま〜す')
        self.assertTrue(actual)
        
        actual = sut.isimgoing(u'いってきー')
        self.assertTrue(actual)
        
        actual = sut.isimgoing(u'いってき〜')
        self.assertTrue(actual)
        
        actual = sut.isimgoing(u'いってき')
        self.assertFalse(actual)
        
if __name__ == '__main__':
    unittest.main()
