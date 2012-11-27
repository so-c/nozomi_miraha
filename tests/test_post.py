# coding: utf-8
import unittest
from models import Post
from xml.dom import minidom

class TestPost(unittest.TestCase):
    def test_get_title(self):
        dom = minidom.parse('tests/data/feed.xml')
        entry_elem = dom.getElementsByTagName('entry')[0]

        post = Post(entry_elem)
        self.assertMultiLineEqual(post.get_title(), u'世界の終わり')

    def test_get_categories(self):
        dom = minidom.parse('tests/data/feed.xml')
        entry_elem = dom.getElementsByTagName('entry')[0]

        post = Post(entry_elem)
        categories = post.get_categories()
        self.assertMultiLineEqual(categories[0], u'鏡館')
        self.assertMultiLineEqual(categories[1], u'写真')

    def test_get_link(self):
        dom = minidom.parse('tests/data/feed.xml')
        entry_elem = dom.getElementsByTagName('entry')[0]

        post = Post(entry_elem)
        self.assertMultiLineEqual(post.get_link(),
            u'http://mirahalibrary.blogspot.com/2012/11/blog-post_22.html')

if __name__ == '__main__':
    unittest.main()
