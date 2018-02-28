# -*- coding: utf-8 -*-
# @CreateTime:  2018/2/28 14:39 
# @CreateBy:    Alvin
# @File:        htmlexport.py
# @UpdateTime:
# @UpdateBy:

import os
from jinja2 import Environment, FileSystemLoader


class HtmlExport(object):

    def __init__(self, hostnames, filename):
        self.hostnames = hostnames
        self.filename = filename

    def write_html(self):
        env = Environment(loader=FileSystemLoader('templates'))
        output_template = env.get_template('export.html')
        output = output_template.render(hostnames=self.hostnames)

        with open(self.filename, "wb") as f:
            f.write(output)


if __name__ == "__main__":
    hts = ['qq.com', 'www.qq.com', 'im.qq.com', 'test.qq.com']
    HtmlExport(hts, 'output.html').write_html()

