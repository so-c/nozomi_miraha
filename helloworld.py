#coding: utf-8
import ConfigParser
import tweepy

CONFIG_FILE = 'config.ini'

config = ConfigParser.SafeConfigParser()
config.read(CONFIG_FILE)

consumer_key        = config.get('consumer', 'key')
consumer_secret     = config.get('consumer', 'secret')
access_token        = config.get('access', 'token')
access_token_secret = config.get('access', 'token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler=auth)

api.update_status(u'おはようございます。')
