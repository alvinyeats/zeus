import requests

from .abs_search import ABSSearch


class BingSearch(ABSSearch):

    def __init__(self,):
        self.server = "http://www.bing.com/searches"

    def get_page(self, word, page_num):
        payload = {'q': '@' + word, 'count': 10, 'first': page_num}
        r = requests.get(self.server, params=payload)
        return r.text
