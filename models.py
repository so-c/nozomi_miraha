# coding: utf-8
from google.appengine.api import mail
from xml.dom import minidom
from tweepy.error import TweepError
from util import MirahaParser
import ConfigParser
import feedparser
import tweepy
import urllib2

CONFIG_FILE = 'config.ini'

# Twitter Account
class Account:

    def __init__(self):
        config = ConfigParser.SafeConfigParser()
        config.read(CONFIG_FILE)

        consumer_key        = config.get('consumer', 'key')
        consumer_secret     = config.get('consumer', 'secret')
        access_token        = config.get('access', 'token')
        access_token_secret = config.get('access', 'token_secret')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth_handler=auth)

    # tweet a messge.
    def tweet(self, message):
        try:
            self.api.update_status(message)
        except TweepError as e:
            message = ErrorNotifier()
            error_message = '{0} when tweet "{1}"'.format(e.reason, message)
            message.notify_error(error_message)
            raise

# Error notifier by email
class ErrorNotifier:

    def __init__(self):
        config = ConfigParser.SafeConfigParser()
        config.read(CONFIG_FILE)

        self.message = mail.EmailMessage()
        self.message.subject = config.get('mail', 'subject')
        self.message.sender  = config.get('mail', 'from')
        self.message.to      = config.get('mail', 'to')

    # send email.
    def notify_error(self, body):
        self.message.body = body
        self.message.check_initialized()
        self.message.send()

# Weather info
# see http://weather.livedoor.com/weather_hacks/webservice.html
class Weather:
    API_URL = 'http://weather.livedoor.com/forecast/webservice/rest/v1?city={0}&day={1}'

    def __init__(self, city_id, day):
        options = ['today', 'tomorrow', 'dayaftertomorrow']
        error_message = 'day must be "today", "tomorrow" or "dayaftertomorrow".'
        if day not in options:
            raise ValueError(error_message)

        self.city_id = city_id
        self.day = day

        self.weather_xml = minidom.parse(urllib2.urlopen(self.get_url()))

    def get_url(self):
        return self.API_URL.format(self.city_id, self.day)

    def get_telop(self):
        return self.weather_xml.getElementsByTagName('telop')[0].firstChild.data

    def get_link(self):
        return self.weather_xml.getElementsByTagName('link')[0].firstChild.data

    def get_pref(self):
        location = self.weather_xml.getElementsByTagName('location')[0]
        return location.attributes['pref'].value

# Blogg class including 25 posts
class Blog:

    def __init__(self, url):
        self.d = feedparser.parse(url)
        self.title = self.d.feed.title

        post_elems = self.d.entries
        num_posts = len(post_elems)
        self.posts = []
        for i in range(num_posts):
            post = Post(post_elems[i])
            self.posts.append(post)

    def get_title(self):
        return self.title

    def get_posts(self):
        return self.posts

# Post class
class Post:
    def __init__(self, entry_elem):
        self.title = entry_elem.title

        tag_elems = entry_elem.tags
        self.tags = []
        num_tags = len(tag_elems)
        for i in range(num_tags):
            attr = tag_elems[i].term
            self.tags.append(attr)

        self.link = entry_elem.feedburner_origlink

        self.content = entry_elem.content[0].value

    def get_title(self):
        return self.title

    def get_tags(self):
        return self.tags

    def get_link(self):
        return self.link

    def get_content(self):
        return self.content

    def get_nozomi_dialogs(self):
        parser = MirahaParser()
        parser.feed(self.content)
        return parser.dialogs
