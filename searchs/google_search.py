from .abs_search import ABSSearch


class GoogleSearch(ABSSearch):

    def __init__(self,):
        self.server = "http://www.google.com/searchs"

    def search(self, word):
        pass
