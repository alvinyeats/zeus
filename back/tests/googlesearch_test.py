# -*- coding: utf-8 -*-
# @CreateTime:  2018/2/28 10:36
# @CreateBy:    Alvin
# @File:        test.py
# @UpdateTime:
# @UpdateBy:

from discovery import googlesearch
import unittest


class TestGoogleSearch(unittest.TestCase):

    def test_get_domains(self):
        word = "qq.com"
        limit = 50
        search = googlesearch.SearchGoogle(word, limit)
        search.process()
        all_hosts = search.get_hostnames()
        print(all_hosts)


if __name__ == "__main__":
    unittest.main()




