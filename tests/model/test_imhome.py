# coding: utf-8
import unittest
from model.imhome import ImHome

class TestImHome(unittest.TestCase):
    def test_isimhome(self):
        sut = ImHome()

        actual = sut.isimhome(u'ただいま')
        self.assertTrue(actual)
        
        actual = sut.isimhome(u'たっだいま')
        self.assertTrue(actual)
        
        actual = sut.isimhome(u'ただいまー')
        self.assertTrue(actual)
        
        actual = sut.isimhome(u'ただいま〜')
        self.assertTrue(actual)
        
if __name__ == '__main__':
    unittest.main()
