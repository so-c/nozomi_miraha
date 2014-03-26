# coding: utf-8
import logging
import webapp2
from models import Account
from util import GreetingExpression
import datetime

class HelloReplier(webapp2.RequestHandler):
    def get(self):
        account = Account()
        timelines = account.followings_timeline()
        names = account.followings_name()
        screen_names = account.followings_screen_name()

        # visits followings
        for userid in timelines.keys():
            # visits each followings' tweets
            for t in timelines[userid]:
                tweetid = t[0]
                tweet = t[1]
                time = t[2]

                logging.debug("name : " + names[userid])
                logging.debug("tweet : " + tweet)
                logging.debug("time : " + time.strftime("%y/%m/%d %H:%M:%S %Z"))
                logging.debug("today: " + datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S %Z"))

                # if the tweets is greet, reply to it
                if self.is_reply(tweet, time):
                    msg = u'@' + screen_names[userid] + u' おはようございます、' + names[userid] + u'さん。'
                    account.reply(msg, tweetid)
                    break

    def is_reply(self, tweet, time):
        greeting_expr = GreetingExpression()
        if not greeting_expr.ismorninggreeting(tweet):
            return False

        if u'@' in tweet:
            return False

        delta = datetime.timedelta(hours=9)
        
        time = time + delta
        today = datetime.datetime.now() + delta
        if time.date() != today.date():
            return False
        
        logging.debug("time : " + time.strftime("%y/%m/%d %H:%M:%S %Z"))
        logging.debug("today: " + today.strftime("%y/%m/%d %H:%M:%S %Z"))

        return True

app = webapp2.WSGIApplication([('/reply-hello', HelloReplier)], debug=false)
