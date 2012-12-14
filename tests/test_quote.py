# coding: utf-8
import unittest
from quote import Quote
from models import Blog
from models import Post

class TestQuote(unittest.TestCase):
    def test_shorten_msg(self):
        quote = Quote()
        s = '''
        1234567890123456789012345678901234567890
        1234567890123456789012345678901234567890
        1234567890123456789012345678901234567890
        1234567890123456789012345678901234567890
        '''
        ss = quote.shorten_msg(s)
        self.assertEquals(len(ss) + 1 + 20, 140)

    def test_unduplicate_msg(self):
        blog = Blog('tests/data/feed.xml')
        post = blog.get_posts()[0]
        post.content = u'<div class="nozomi">duplicates</div>'
        post.link = 'http://hoge.com/fuga.html'

        quote = Quote()
        last_tweet = u'duplicates http://hoge.com/fuga.html'
        posts = [post]

        # 同じセリフしか見つからない場合
        msg = quote.unduplicate_msg(last_tweet, posts)
        self.assertMultiLineEqual(msg, u'前回と違うつぶやきが見つかりません……。')

        # 違うセリフが見つかる場合
        post.content = u'<div class="nozomi">duplicates</div><div class="nozomi">new</div>'
        msg = quote.unduplicate_msg(last_tweet, posts)
        self.assertMultiLineEqual(msg, u'new http://hoge.com/fuga.html')

if __name__ == '__main__':
    unittest.main()
