# -*- coding: utf-8 -*-

import socket


class Checker(object):

    def __init__(self, hosts):
        self.hosts = hosts
        self.realhosts = []

    def check(self):
        for x in self.hosts:
            try:
                res = socket.gethostbyname(x)
                self.realhosts.append(res + ":" + x)
            except Exception as e:
                pass
        return self.realhosts


if __name__ == "__main__":
    full_host = Checker(['www.qq.com', 'mail.qq.com'])
    full = full_host.check()
    print full
