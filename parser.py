# -*- coding: utf-8 -*-
# @CreateTime:  2018/2/27 10:54 
# @CreateBy:    Alvin
# @File:        parser.py
# @UpdateTime:
# @UpdateBy:

import re


class Parser(object):

    def __init__(self, results, word):
        self.results = results
        self.word = word
        self.temp = []

    def hostnames(self):
        reg_hosts = re.compile('[a-zA-Z0-9.-]*\.' + self.word)
        self.temp = reg_hosts.findall(self.results)
        hostnames = self.unique()
        return hostnames

    def unique(self):
        new = []
        for x in self.temp:
            if x not in new:
                new.append(x)
        return new
