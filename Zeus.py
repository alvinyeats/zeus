# -*- coding: utf-8 -*-
# @CreateTime:  2018/3/1 13:27 
# @CreateBy:    Alvin
# @File:        Zeus.py
# @UpdateTime:
# @UpdateBy:
import getopt
import os
import sys
import traceback

from discovery import *
from lib import htmlexport
from lib import hostchecker

print "\n***************************"
print "*  ____  ___  __  _______ *"
print "* /_  / / _ \/ / / / ___/ *"
print "*  / /_/  __/ /_/ (__  )  *"
print "* /___/\___/\__,_/____/   *"
print "***************************\n\n"


def usage():
    comm = os.path.basename(sys.argv[0])

    print "Usage: Zeus options \n"
    print "     -d: Domain to search or company name"
    print "     -b: data source: baidu, bing, google, all\n"
    print "     -f: Save the results into an HTML"
    print "     -l: Limit the number of results to work with"
    print "     -h: Get help"
    print "\nExamples:"
    print "     " + comm + " -d qq.com -l 500 -b baidu -f result.html"


def start(argv):
    if len(sys.argv) < 5:
        usage()
        sys.exit()
    try:
        opts, args = getopt.getopt(argv, "hl:d:b:f:")
    except getopt.GetoptError:
        usage()
        sys.exit()
    word = ""
    engine = ""
    filename = ""
    limit = 100
    all_hosts = []
    full = []
    for opt, arg in opts:
        if opt == '-l':
            limit = int(arg)
        elif opt == '-d':
            word = arg
        elif opt == '-b':
            engine = arg
            if engine not in ("baidu", "bing"):
                usage()
                print "Invalid search engine, try with: baidu/bing, other waiting to add ..."
                sys.exit()
            else:
                pass
        elif opt == '-f':
            filename = arg
    if engine == "baidu":
        print "[-] Searching in Baidu:"
        search = baidusearch.SearchBaidu(word, limit)
        search.process()
        all_hosts = search.get_hostnames()
    elif engine == "bing":
        print "[-] Searching in Bing:"
        search = bingsearch.SearchBing(word, limit)
        search.process()
        all_hosts = search.get_hostnames()

    # ************* Results ******************
    print "\n[+] Hosts found in search engines:"
    print "------------------------------------"
    if not all_hosts:
        print "No hosts found"
    else:
        all_hosts = sorted(set(all_hosts))
        print "[-] Resolving hostnames IPs... "
        full_host = hostchecker.Checker(all_hosts)
        full = full_host.check()
        for host in full:
            print host

    # ************* Reporting ******************
    if filename != "":
        try:
            print "\n[+] Saving files..."
            html = htmlexport.HtmlExport(word, full, filename)
            html.write_html()
        except:
            print traceback.print_exc()
            print "Error creating the file"
        # todo create xml report
        sys.exit()


if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print "Search interrupted by user.."
    except:
        sys.exit()
