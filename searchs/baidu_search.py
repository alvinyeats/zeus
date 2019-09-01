import time

import requests

from .abs_search import ABSSearch


class BaiDuSearch(ABSSearch):

    def __init__(self, word, page_limit):
        self.server = "http://www.baidu.com/s"
        self.page_limit = page_limit
        self.counter = 0
        self.word = word
        self.total_results = ""

    def do_search(self):
        payload = {'wd': '@' + self.word, 'pn': self.counter}
        r = requests.get(self.server, params=payload)
        self.total_results += r.text

    def process(self):
        while self.counter <= self.page_limit and self.counter <= 1000:
            self.do_search()
            time.sleep(1)

            print("\tSearching " + str(self.counter) + " results...")
            self.counter += 10


