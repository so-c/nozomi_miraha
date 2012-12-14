# coding: utf-8
import unittest
from util import Holiday
import datetime

class TestQuote(unittest.TestCase):
    def test_isholidy(self):
        holiday = Holiday()
        actual = holiday.isholiday(datetime.date(2012, 1, 2))
        self.assertEquals('', actual)
        actual = holiday.isholiday(datetime.date(2012, 1, 1))
        self.assertEquals(u'元日', actual)

if __name__ == '__main__':
    unittest.main()
