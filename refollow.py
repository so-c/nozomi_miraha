# coding: utf-8
import webapp2
from models import Account

class Refollow(webapp2.RequestHandler):
    def get(self):
        account = Account()
        account.refollow()

app = webapp2.WSGIApplication([('/refollow', Refollow)], debug=True)
