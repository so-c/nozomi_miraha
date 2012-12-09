# coding: utf-8
import webapp2
import random
from models import Account
from models import Blog
from models import Post

class Quote(webapp2.RequestHandler):
    def get(self):
        blog = Blog('http://mirahalibrary.blogspot.com/feeds/posts/default')
        posts = blog.select_posts_bytag(u'鏡館')

        len_posts = len(posts)
        if len_posts <= 0:
            # TODO 引用するつぶやきがない場合
            pass
        else:
            pairs = []
            for p in posts:
                dialogs = p.get_nozomi_dialogs()
                for d in dialogs:
                    pairs.append((d, p.get_link()))

            lr = random.randint(0, len(pairs) - 1)
            line = pairs[lr][0]
            link = pairs[lr][1]

            msg = self.shorten_msg(line) + ' ' + link

            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write(msg)

        account = Account()
        # account.tweet(msg)

    def shorten_msg(self, line):
        len_limit = 140 - 20 - 1  # XXX remove magic number
        if(len(line) <= len_limit):
            return line
        else:
            return line[0:(len_limit - 2)] + u'…」'

app = webapp2.WSGIApplication([('/quote', Quote)], debug=True)
