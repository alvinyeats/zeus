# -*- coding: utf-8 -*-
# @CreateTime:  2018/2/27 10:42 
# @CreateBy:    Alvin
# @File:        baidusearch.py
# @UpdateTime:
# @UpdateBy:

import requests
import time

import myparser


class SearchBaidu(object):

    def __init__(self, word, limit):
        self.word = word
        self.total_results = ""
        self.server = "http://www.baidu.com/s"
        self.limit = limit
        self.counter = 0

    def do_search(self):
        payload = {'wd': '@'+self.word, 'pn': self.counter}
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

