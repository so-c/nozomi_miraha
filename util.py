# coding: utf-8
from HTMLParser import HTMLParser
import datetime
import ConfigParser
import urllib2
import re
from django.utils import simplejson

class MirahaParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__is_nozomi = False
        self.__current_str = ''
        self.dialogs = []

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            attrs = dict(attrs)
            if 'class' in attrs and attrs['class'].find('nozomi') > -1:
                self.__is_nozomi = True

    def handle_endtag(self, tag):
        if self.__is_nozomi and tag == 'div':
            self.__is_nozomi = False
            self.dialogs.append(self.__current_str)
            self.__current_str = ''

    def handle_data(self, data):
        if self.__is_nozomi:
            self.__current_str += data

class Holiday():
    def __init__(self):
        config = ConfigParser.SafeConfigParser()
        CONFIG_FILE = 'config.ini'
        config.read(CONFIG_FILE)

        baseurl = 'https://www.googleapis.com/calendar/v3/calendars/'
        calendarid = 'ja.japanese%23holiday@group.v.calendar.google.com'
        key = config.get('google', 'key')
        self.url = baseurl + calendarid + '/events' + '?key=' + key

    def isholiday(self, dt):
        req = self.buildurl(dt)
        js = simplejson.load(urllib2.urlopen(req))
        if js['items']:
            return js['items'][0]['summary']
        else:
            return ''

    def buildurl(self, dt):
        d = datetime.datetime(dt.year, dt.month, dt.day, 0, 0, 0, 0)
        timemin = 'timeMin=' + d.isoformat() + 'Z'
        timemax = 'timeMax=' + (d + datetime.timedelta(days=1)).isoformat() + 'Z'
        maxresults = 'maxResults=' + '1'
        singleevents = 'singleEvents=' + 'true'
        req = '&'.join([self.url, timemin, timemax, maxresults, singleevents])
        return req

class GreetingExpression():
    def __init__(self):
        self.__morning_ge1 = re.compile(u'(おはよ?う?|オハヨ?ウ?)(ー|〜)?')
        self.__morning_ge2 = re.compile(u'ぐっど?もーにんぐ?|グッド?モーニング?')

    def ismorninggreeting(self, text):
        is1 = self.__morning_ge1.search(text) != None
        is2 = self.__morning_ge2.search(text) != None
        return is1 or is2
