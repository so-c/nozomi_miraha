# coding: utf-8
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
                # if the tweets is greet, reply to it
                if self.is_reply(tweet, time):
                    msg = u'@' + screen_names[userid] + u' おはようございます、' + names[userid] + u'さん。'
                    account.reply(msg, tweetid)
                    break

    def is_reply(self, tweet, time):
        greeting_expr = GreetingExpression()
        if not greeting_expr.ismorninggreeting(tweet):
            return False
        if not u'@' in tweet:
            return False
        today = datetime.datetime.combine(datetime.date.today(), datetime.time(0))
        if time < today:
            return False
        return True

app = webapp2.WSGIApplication([('/reply-hello', HelloReplier)], debug=True)
