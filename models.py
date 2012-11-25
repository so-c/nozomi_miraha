#coding: utf-8
import ConfigParser
import tweepy
from tweepy.error import TweepError
from google.appengine.api import mail

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
            message.notify_error()
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
