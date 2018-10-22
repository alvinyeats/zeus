# -*- coding: utf-8 -*-
# @CreateTime:  2018/2/28 14:39 
# @CreateBy:    Alvin
# @File:        htmlexport.py
# @UpdateTime:
# @UpdateBy:

import os
from jinja2 import Environment, FileSystemLoader


class HtmlExport(object):

    def __init__(self, domain, hosts, filename):
        self.domain = domain
        self.hosts = hosts
        self.filename = filename

    def write_html(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        tem_dir = os.path.join(base_dir, 'templates')
        env = Environment(loader=FileSystemLoader(tem_dir))
        output_template = env.get_template('export.html')
        output = output_template.render(domain=self.domain, hosts=self.hosts)

        with open(self.filename, "wb") as f:
            f.write(output)


# test
if __name__ == "__main__":
    hts = ['qq.com', 'www.qq.com', 'im.qq.com', 'test.qq.com']
    HtmlExport('qq.com', hts, 'output.html').write_html()
