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

        msg = self.sample_msg(posts)
        account = Account()
        last_status = account.api.user_timeline(count=1)[0].text

        logging.info('last status: ' + last_status)
        logging.info('msg: ' + msg)

        i = 0
        while msg == last_status and i < 10:
            msg = self.sample_msg(posts)
            logging.info('msg: ' + msg)
            i += 1

        if i == 10:
            msg = u'前回と違うつぶやきが見つかりません……。'

        account.tweet(msg)

    def sample_msg(self, posts):
        len_posts = len(posts)
        if len_posts <= 0:
            return u'最近は、鏡館に遊びに行っていないです。久しぶりに行ってみようかな？'
        else:
            pairs = []
            for p in posts:
                dialogs = p.get_nozomi_dialogs()
                for d in dialogs:
                    pairs.append((d, p.get_link()))

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
