import requests

from .abs_search import ABSSearch


class BaiDuSearch(ABSSearch):

    def __init__(self):
        self.server = "http://www.baidu.com/s"

    def get_page(self, word, page_num):
        payload = {'wd': '@' + word, 'pn': page_num}
        r = requests.get(self.server, params=payload)
        return r.text



