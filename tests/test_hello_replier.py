# coding: utf-8
import unittest
from hello_replier import HelloReplier
import datetime

class TestHelloReplier(unittest.TestCase):
    def test_is_reply_when_unmatch_text(self):
        replier = HelloReplier()
        text = u'test'
        time = datetime.datetime.today()
        self.assertFalse(replier.is_reply(text, time))

    def test_is_reply_when_not_include_at(self):
        replier = HelloReplier()
        text = u'おはよう'
        time = datetime.datetime.today()
        self.assertFalse(replier.is_reply(text, time))

    def test_is_reply_when_not_today(self):
        replier = HelloReplier()
        text = u'@nozomi_miraha おはよう'
        time = datetime.datetime(2000, 1, 1)
        self.assertFalse(replier.is_reply(text, time))

    def test_is_reply_when_true(self):
        replier = HelloReplier()
        text = u'@nozomi_miraha おはよう'
        time = datetime.datetime.today()
        self.assertTrue(replier.is_reply(text, time))

if __name__ == '__main__':
    unittest.main()
