# coding: utf-8
import unittest
from models import Blog

class TestBlog(unittest.TestCase):
    def test_get_title(self):
        blog = Blog('tests/data/feed.xml')
        self.assertMultiLineEqual(blog.get_title(), 'Mirror House Annex')

    def test_get_posts(self):
        blog = Blog('tests/data/feed.xml')
        post = blog.get_posts()[0]

        self.assertMultiLineEqual(post.get_title(), u'世界の終わり')
        self.assertMultiLineEqual(post.get_tags()[0], u'鏡館')
        self.assertMultiLineEqual(post.get_tags()[1], u'写真')

if __name__ == '__main__':
    unittest.main()
