# coding: utf-8
import unittest
from models import Post
from xml.dom import minidom
import feedparser

class TestPost(unittest.TestCase):
    def test_get_title(self):
        d = feedparser.parse('tests/data/feed.xml')
        entry_elem = d.entries[0]

        post = Post(entry_elem)
        self.assertMultiLineEqual(post.get_title(), u'世界の終わり')

    def test_get_tags(self):
        d = feedparser.parse('tests/data/feed.xml')
        entry_elem = d.entries[0]

        post = Post(entry_elem)
        tags = post.get_tags()
        self.assertMultiLineEqual(tags[0], u'鏡館')
        self.assertMultiLineEqual(tags[1], u'写真')

    def test_get_link(self):
        d = feedparser.parse('tests/data/feed.xml')
        entry_elem = d.entries[0]

        post = Post(entry_elem)
        self.assertMultiLineEqual(post.get_link(),
            u'http://mirahalibrary.blogspot.com/2012/11/blog-post_22.html')

    def test_get_content(self):
        d = feedparser.parse('tests/data/feed.xml')
        entry_elem = d.entries[0]

        post = Post(entry_elem)
        print post.get_content()

    def test_get_nozomi_dialgs(self):
        d = feedparser.parse('tests/data/feed.xml')
        entry_elem = d.entries[0]

        post = Post(entry_elem)
        self.assertMultiLineEqual(post.get_nozomi_dialog()[0],
            u'「原種・亜種と同じく飛び回ったり走り回ったりして追うのが大変なのに、希少種ときたら頭も硬いのが厄介ですよね」')

if __name__ == '__main__':
    unittest.main()
