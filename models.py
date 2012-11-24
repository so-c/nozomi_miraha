import ConfigParser
import tweepy

# Twitter Account
class Account:
    # login info
    CONFIG_FILE = 'config.ini'

    def __init__(self):
        config = ConfigParser.SafeConfigParser()
        config.read(self.CONFIG_FILE)

        consumer_key        = config.get('consumer', 'key')
        consumer_secret     = config.get('consumer', 'secret')
        access_token        = config.get('access', 'token')
        access_token_secret = config.get('access', 'token_secret')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth_handler=auth)

    def tweet(self, message):
        self.api.update_status(message)
