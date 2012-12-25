# coding: utf-8
import unittest
from util import GreetingExpression

class TestGreetingExpression(unittest.TestCase):
    def test_ismorninggreeting(self):
        ge = GreetingExpression()

        actual = ge.ismorninggreeting(u'おはよ')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'おはよう')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'おはよー')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'おはよ〜')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'おはようー')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'おはよう〜')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'オハヨ')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'オハヨウ')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'オハヨー')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'オハヨ〜')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'オハヨウー')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'オハヨウ〜')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'ぐっどもーにんぐ')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'ぐっもーにん')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'グッドモーニング')
        self.assertTrue(actual)

        actual = ge.ismorninggreeting(u'グッモーニン')
        self.assertTrue(actual)

if __name__ == '__main__':
    unittest.main()
