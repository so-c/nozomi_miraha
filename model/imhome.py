# coding: utf-8
import re

class ImHome():
    ''' 「ただいま」を意味する正規表現とそのチェック '''
    def __init__(self):
        self.__imhome1 = re.compile(u'たっ?だいま(ー|〜)?')

    def isimhome(self, text):
        ''' textが「ただいま」を表してればtrue '''
        is1 = self.__imhome1.search(text) != None
        return is1