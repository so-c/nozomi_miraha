#coding: utf-8
import sys
import webapp2
import random
from models import Account
from models import Weather

weather = Weather(63, 'today')
telop = weather.get_telop()

if telop.find(u'雨') != -1:
    msg_tmpl = u'おはようございます。今日は{0}ですね。傘はお持ちですか? {1}'
    msg = msg_tmpl.format(telop, weather.get_link())

if telop.find(u'雪') != -1:
    msg_tmpl = u'おはようございます。今日は{0}ですよ！ 暖かくしていってくださいね。 {1}'
    msg = msg_tmpl.format(telop, weather.get_link())

else:
    random.seed()
    r = random.randint(0, 2)

    if r == 0:
        msg = u'おはようございます。今日も1日がんばりましょう。'
    elif r == 1:
        msg = u'おはようございます。今日は何しようかな？'
    elif r == 2:
        msg = u'おはようございまーす♪'

account = Account()
account.tweet(msg)
