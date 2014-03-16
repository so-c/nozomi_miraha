# coding: utf-8
import webapp2
from models import Account
from model.imhome import ImHome
import datetime

class WelcomeBack(webapp2.RequestHandler):
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
                # if the tweets is imhome, reply to it
                if self.is_reply(tweet, time):
                    msg = u'@' + screen_names[userid] + u' おかえりなさい、' + names[userid] + u'さん。'
                    account.reply(msg, tweetid)
                    break

    def is_reply(self, tweet, time):
        imhome_expr = ImHome()
        if not imhome_expr.isimhome(tweet):
            return False
        
        if u'@' in tweet:
            return False

        delta = datetime.datetime.now() - time
        if delta.seconds >= 5 * 60:
            return False
        return True

app = webapp2.WSGIApplication([('/welcome-back', WelcomeBack)], debug=True)
