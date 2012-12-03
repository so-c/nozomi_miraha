# coding: utf-8
import webapp2
import random
from page import InfoPage
from models import Account
from models import Blog
from models import Post

app = webapp2.WSGIApplication([('/quote', InfoPage)], debug=True)

blog = Blog('http://mirahalibrary.blogspot.com/feeds/posts/default')
posts = blog.select_posts_bytag(u'鏡館')

len_posts = len(posts)
if len_posts <= 0:
    # TODO 引用するつぶやきがない場合
    msg = 'test.'
    pass
else:
    random.seed()
    pr = random.randint(0, len_posts - 1)
    post = posts[pr]

    lines = post.get_nozomi_dialogs()
    lr = random.randint(0, len(lines) - 1)
    line = lines[lr]

    len_limit = 140 - 20 - 1# TODO remove magic number
    msg = line[0:len_limit] + ' ' + post.get_link()

account = Account()
account.tweet(msg)
