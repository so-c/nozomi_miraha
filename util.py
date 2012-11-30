# coding: utf-8
from HTMLParser import HTMLParser

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
