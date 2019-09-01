import requests

from .abs_search import ABSSearch


class GoogleSearch(ABSSearch):

    def __init__(self,):
        self.server = "http://www.google.com/search"

    def get_page(self, word, page_num):
        payload = {'q': 'site:' + word, 'start': page_num, 'num': 10}
        r = requests.get(self.server, params=payload)
        print(r.request)
        return r.text
