# coding: utf-8
import webapp2
import random
from models import Account

class GoodNight(webapp2.RequestHandler):
    def get(self):
        random.seed()
        r = random.randint(0, 2)

        if r == 0:
            msg = u'眠たくなってきました……。おやすみなさい。'
        elif r == 1:
            msg = u'おやすみなさい。あまり夜更かしすると体に毒ですよ？'
        elif r == 2:
            msg = u'明日に備えて、そろそろ寝ることにします。おやすみなさい。'

        account = Account()
        account.tweet(msg)

app = webapp2.WSGIApplication([('/good-night', GoodNight)], debug=True)
