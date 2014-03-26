# coding: utf-8
import re

class ImGoing():
    ''' 「いってきます」を意味する正規表現とそのチェック '''
    def __init__(self):
        self.__imgoing = re.compile(u'いってき((ー|〜)|(ま(ー|〜)?っ?す))')

    def isimgoing(self, text):
        ''' textが「いってきます」を表してればtrue '''
        is1 = self.__imgoing.search(text) != None
        return is1