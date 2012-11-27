# coding: utf-8
import unittest
from models import Blog

class TestBlog(unittest.TestCase):
    def test_get_title(self):
        blog = Blog('http://mirahalibrary.blogspot.com/feeds/posts/default')
        self.assertMultiLineEqual(blog.get_title(), 'Mirror House Annex')

if __name__ == '__main__':
    unittest.main()
