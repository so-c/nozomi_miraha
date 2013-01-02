# coding: utf-8
import unittest
from models import Account

class TestAccount(unittest.TestCase):
    def test_followings_timeline(self):
        account = Account()
        tweets = account.followings_timeline()
        myid = 43657148
        self.assertTrue(myid in tweets)
        self.assertTrue(len(tweets[myid]) > 0)
        print tweets[myid][0][0]
        print tweets[myid][0][1]

    def test_followings_name(self):
        account = Account()
        names = account.followings_name()
        myid = 43657148
        self.assertTrue(myid in names)
        self.assertEquals(names[43657148], u'鏡双司')

    def test_followings_screen_name(self):
        account = Account()
        screen_names = account.followings_screen_name()
        myid = 43657148
        self.assertTrue(myid in screen_names)
        self.assertEquals(screen_names[43657148], u'SO_C')

if __name__ == '__main__':
    unittest.main()
