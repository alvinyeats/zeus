# -*- coding: utf-8 -*-

from __future__ import unicode_literals
# from apps.mails.models import SubscribeMail

# CNNVD && NVD关键字， 用于获取信息时，对信息台南家敏感词标签
CVE_KEY_WORDS = ['java', 'tomcat', 'apache', 'linux', 'nginx', 'PHP', 'MYSQL',
                 'SSH', 'windows', 'IIS', 'struts2', 'sql server', 'oracle',
                 'elasticsearch', 'jira', 'wordpress', 'rabbitmq', 'activemq', 'dubbo', 'zookeeper', 'pvk']

# CNNVD&NVD关键字。不区分大小写
CVE_KEY_WORDS1 = [r'\bjava\b', r'\btomcat\b', r'\bapache\b', r'\blinux\b', r'\bnginx\b', r'\bPHP\b', r'\bMYSQL\b',
                  r'\bSSH\b', r'\bwindows\b', r'\bIIS\b', r'\bstruts2\b', r'\bsql server\b', r'\boracle\b',
                  r'\belasticsearch\b', r'\bjira\b', r'\bwordpress\b', r'\brabbitmq\b', r'\bactivemq\b', r'\bdubbo\b',
                  r'\bzookeeper\b', r'\bpvk\b']
