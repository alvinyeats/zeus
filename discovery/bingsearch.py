# -*- coding: utf-8 -*-
# @CreateTime:  2018/3/13 18:24 
# @CreateBy:    Alvin
# @File:        bingsearch.py
# @UpdateTime:
# @UpdateBy:

import requests
import time

import myparser


class SearchBing(object):

    def __init__(self, word, limit):
        self.word = word
        self.total_results = ""
        self.server = "http://www.bing.com/search"
        self.limit = limit
        self.counter = 0

    def do_search(self):
        payload = {'q': '@'+self.word, 'count': 50, 'first': self.counter}
        r = requests.get(self.server, params=payload)
        self.total_results += r.text

    def process(self):
        while self.counter <= self.limit and self.counter <= 1000:
            self.do_search()
            time.sleep(1)

            print("\tSearching " + str(self.counter) + " results...")
            self.counter += 10

    def get_hostnames(self):
        raw_res = myparser.Parser(self.total_results, self.word)
        return raw_res.hostnames()


