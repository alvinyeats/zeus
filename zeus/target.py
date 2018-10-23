# -*- coding: UTF-8 -*-

"""
    target
    ~~~

    Domain target parser and management

    :author:    Alvin <alvinyeats@gmail.com>
    :homepage:  https://github.com/alvinyeats/zeus
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2018 Alvin. All rights reserved
"""

import queue


class Target(object):

    def __init__(self):
        self.targets = queue.Queue()

    def add(self, target):
        self.targets.put(target)

    def get(self):
        return self.targets.get()

    def remove(self):
        pass
