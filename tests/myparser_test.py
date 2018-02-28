# -*- coding: utf-8 -*-
# @CreateTime:  2018/2/28 10:35 
# @CreateBy:    Alvin
# @File:        myparser_test.py
# @UpdateTime:
# @UpdateBy:

import myparser
import unittest


class TestParser(unittest.TestCase):

    def test_hostnames(self):
        word = "qq.com"
        results = "@chuangshi.qq.com****test.im.qq.com**fskfhqefm,nfuq!@#$!^#$^&mail.qq.com"
        p = myparser.Parser(results, word)
        hostnames = sorted(p.hostnames())
        print hostnames
        self.assertEqual(hostnames, ['chuangshi.qq.com', 'mail.qq.com', 'test.im.qq.com'])

if __name__ == '__main__':
    unittest.main()


