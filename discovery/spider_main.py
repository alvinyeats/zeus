# -*- coding: utf-8 -*-
# @CreateTime:  2018/2/27 9:27 
# @CreateBy:    Alvin
# @File:        spider_main.py
# @UpdateTime:
# @UpdateBy:

from __future__ import unicode_literals

import re
import requests


def collection(url):
    response = requests.get(url).content
    # sub_domain = re.findall('style="text-decoration:none;">(.*?)/', response)
    print response

if __name__ == "__main__":
    target = 'http://www.baidu.com/s?wd=site:qq.com'
    collection(target)
