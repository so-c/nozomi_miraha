# coding: utf-8
import unittest
from models import Blog

class TestBlog(unittest.TestCase):
    def test_title(self):
        blog = Blog('tests/data/feed.xml')
        self.assertMultiLineEqual(blog.title, 'Mirror House Annex')

    def test_posts(self):
        blog = Blog('tests/data/feed.xml')
        post = blog.posts[0]

        self.assertMultiLineEqual(post.title, u'世界の終わり')
        self.assertMultiLineEqual(post.tags[0], u'鏡館')
        self.assertMultiLineEqual(post.tags[1], u'写真')

    def test_get_select_posts_bytag(self):
        blog = Blog('tests/data/feed.xml')

        selected = blog.select_posts_bytag(u'鏡館')

        for p in selected:
            self.assertTrue(u'鏡館' in p.tags)

if __name__ == '__main__':
    unittest.main()
