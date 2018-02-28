# -*- coding: utf-8 -*-
# @CreateTime:  2018/2/28 10:36
# @CreateBy:    Alvin
# @File:        test.py
# @UpdateTime:
# @UpdateBy:

from discovery import baidusearch
import unittest


class TestBaiDuSearch(unittest.TestCase):

    def test_get_domains(self):
        word = "qq.com"
        limit = 50
        search = baidusearch.SearchBaidu(word, limit)
        search.process()
        all_hosts = search.get_hostnames()
        print all_hosts


if __name__ == "__main__":
    unittest.main()




