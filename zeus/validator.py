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

import socket


def is_host(target):
    target = target.strip()
    try:
        socket.gethostbyname(target)
        return True
    except socket.gaierror:
        return False
