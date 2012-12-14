# coding: utf-8
import webapp2
import random
import datetime
from models import Account
from util import Holiday
import logging

class GoodNight(webapp2.RequestHandler):
    def get(self):
        random.seed()
        r = random.randint(0, 2)

        if r == 0:
            msg = u'眠たくなってきました……。おやすみなさい。'
        elif r == 1:
            msg = u'おやすみなさい。あまり夜更かしすると体に毒ですよ？'
        elif r == 2:
            msg = u'そろそろ寝ることにします。おやすみなさい。'

        d = datetime.datetime.now() + datetime.timedelta(days=1)
        logging.info('now: ' + d.isoformat())
        logging.info('now: ' + str(d.weekday()))

        if d.weekday() == 5:
            msg += u'明日は土曜日、お休みですね。'
        elif d.weekday() == 6:
            msg += u'明日は日曜日、お休みですね。'
        else:
            holiday = Holiday().isholiday(d)
            if holiday != '':
                msg += '明日は' + holiday + '、お休みですね。'

        account = Account()
        account.tweet(msg)

app = webapp2.WSGIApplication([('/good-night', GoodNight)], debug=True)
