#coding: utf-8
import random
from models import Account

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
