# coding: utf-8
import unittest
from models import Weather

class TestWeather(unittest.TestCase):
    def test_get_url(self):
        weather = Weather(130010)

        self.assertMultiLineEqual(
            weather.get_url(),
            'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010')

    def test_get_telop(self):
        weather = Weather(130010)
        print weather.get_telop()

    def test_get_link(self):
        weather = Weather(130010)
        self.assertMultiLineEqual(
            weather.get_link(),
            'http://weather.livedoor.com/area/forecast/130010')

    def test_get_pref(self):
        weather = Weather(130010)
        self.assertMultiLineEqual(
            weather.get_pref(),
            u'東京都')

if __name__ == '__main__':
    unittest.main()
