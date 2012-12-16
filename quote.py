# coding: utf-8
import webapp2
import random
from models import Account
from models import Blog
from models import Post
import logging

class Quote(webapp2.RequestHandler):
    def get(self):
        blog = Blog('http://mirahalibrary.blogspot.com/feeds/posts/default')
        posts = blog.select_posts_bytag(u'鏡館')

        account = Account()
        last_tweet = account.last_tweet()

        msg = self.unduplicate_msg(last_tweet, posts)

        account.tweet(msg)

    def unduplicate_msg(self, last_tweet, posts):
        msg = self.sample_msg(posts)
        i = 0
        while msg == last_tweet and i < 10:
            msg = self.sample_msg(posts)
            i += 1
        if i == 10:
            msg = u'前回と違うつぶやきが見つかりません……。'
        return msg

    def sample_msg(self, posts):
        len_posts = len(posts)
        if len_posts <= 0:
            return u'最近は、鏡館に遊びに行っていないです。久しぶりに行ってみようかな？'
        else:
            for p in posts:
                pairs = [(d, p.link) for d in p.get_nozomi_dialogs()]

            lr = random.randint(0, len(pairs) - 1)
            line = pairs[lr][0]
            link = pairs[lr][1]

            return self.shorten_msg(line) + ' ' + link

    def shorten_msg(self, line):
        len_limit = 140 - 20 - 1  # XXX remove magic number
        if(len(line) <= len_limit):
            return line
        else:
            return line[0:(len_limit - 2)] + u'…」'

app = webapp2.WSGIApplication([('/quote', Quote)], debug=True)
