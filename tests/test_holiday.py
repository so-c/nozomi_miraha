# coding: utf-8
import unittest
from util import Holiday
import datetime

class TestHoliday(unittest.TestCase):
    def test_isholidy_workday_return_empty(self):
        holiday = Holiday()
        actual = holiday.isholiday(datetime.date(2012, 1, 4))
        self.assertEquals('', actual)
        
    def test_isholidy_holiday_return_name(self):
        holiday = Holiday()

        actual = holiday.isholiday(datetime.date(2012, 1, 1))
        self.assertEquals(u'元日', actual)

if __name__ == '__main__':
    unittest.main()
