# coding: utf-8
from google.appengine.api import mail
import json
from tweepy.error import TweepError
from util import MirahaParser
import ConfigParser
from lib import feedparser
import tweepy
import urllib2
import logging

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
        self.__api = tweepy.API(auth_handler=auth)

    # tweet a message.
    def tweet(self, message):
        try:
            self.__api.update_status(message)
            logging.info("tweeted " + message)
        except TweepError as e:
            message = ErrorNotifier()
            error_message = '{0} when tweet "{1}"'.format(e.reason, message)
            message.notify_error(error_message)
            raise

    # reply a message.
    def reply(self, message, status_id):
        assert '@' in message
        try:
            self.__api.update_status(message, in_reply_to_status_id=status_id)
        except TweepError as e:
            message = ErrorNotifier()
            error_message = '{0} when tweet "{1}"'.format(e.reason, message)
            message.notify_error(error_message)
            raise

    # get the last own status.
    def last_tweets(self, count=1):
        return [s.text for s in self.__api.user_timeline(count=count)]

    # refollow followees
    def refollow(self):
        followees_ids = set(self.__api.followers_ids())
        followings_ids = set(self.__api.friends_ids())

        for f in followees_ids - followings_ids:
            self.__api.create_friendship(f)

    # get following users id -> 19 tweets dictionary
    def followings_timeline(self):
        followings_ids = self.__api.friends_ids()
        id_tweets = dict()
        for f in followings_ids:
            tweets = self.__api.get_user(f).timeline()
            id_tweets[f] = [(t.id, t.text, t.created_at) for t in tweets]
        return id_tweets

    # get following user's id -> name dictionary
    def followings_name(self):
        followings_ids = self.__api.friends_ids()
        id_names = dict()
        for i in followings_ids:
            id_names[i] = self.__api.get_user(i).name
        return id_names

    # get following user's id -> screenname dictionary
    def followings_screen_name(self):
        followings_ids = self.__api.friends_ids()
        id_screen_names = dict()
        for i in followings_ids:
            id_screen_names[i] = self.__api.get_user(i).screen_name
        return id_screen_names

# Error notifier by email
class ErrorNotifier:

    def __init__(self):
        config = ConfigParser.SafeConfigParser()
        config.read(CONFIG_FILE)

        self.__message = mail.EmailMessage()
        self.__message.subject = config.get('mail', 'subject')
        self.__message.sender  = config.get('mail', 'from')
        self.__message.to      = config.get('mail', 'to')

    # send email.
    def notify_error(self, body):
        self.__message.body = body
        self.__message.check_initialized()
        self.__message.send()

# Weather info
# see http://weather.livedoor.com/weather_hacks/webservice.html
class Weather:
    __API_URL = 'http://weather.livedoor.com/forecast/webservice/json/v1?city={0}'

    def __init__(self, city_id):
        self.__city_id = city_id

        self.__weather = json.loads(urllib2.urlopen(self.get_url()).read())

    def get_url(self):
        return self.__API_URL.format(self.__city_id)

    def get_telop(self):
        today_index = 0
        return self.__weather.get('forecasts')[today_index].get('telop')

    def get_link(self):
        return self.__weather.get('link')

    def get_pref(self):
        return self.__weather.get('location').get('prefecture')

# Blogg class including 25 posts
class Blog:

    def __init__(self, url):
        self.__d = feedparser.parse(url)
        self.__title = self.__d.feed.title

        post_elems = self.__d.entries
        self.__posts = [Post(p) for p in post_elems]

    @property
    def title(self):
        return self.__title

    @property
    def posts(self):
        return self.__posts

    def select_posts_bytag(self, tag):
        selected = [p for p in self.__posts if tag in p.tags]
        return selected

# Post class
class Post:
    def __init__(self, entry_elem):
        self.__title = entry_elem.title
        self.__tags = [t.term for t in entry_elem.tags]
        self.__link = entry_elem.feedburner_origlink
        self.__content = entry_elem.content[0].value

    @property
    def title(self):
        return self.__title

    @property
    def tags(self):
        return self.__tags

    @property
    def link(self):
        return self.__link

    @property
    def content(self):
        return self.__content

    def get_nozomi_dialogs(self):
        parser = MirahaParser()
        parser.feed(self.content)
        return parser.dialogs
