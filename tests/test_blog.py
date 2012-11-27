# coding: utf-8
import unittest
from models import Blog

class TestBlog(unittest.TestCase):
    def test_get_title(self):
        blog = Blog('http://mirahalibrary.blogspot.com/feeds/posts/default')
        self.assertMultiLineEqual(blog.get_title(), 'Mirror House Annex')

    def test_get_posts(self):
        blog = Blog('http://mirahalibrary.blogspot.com/feeds/posts/default')
        print blog.get_posts()[0].get_title()
        for c in blog.get_posts()[0].get_categories():
            print c

if __name__ == '__main__':
    unittest.main()
