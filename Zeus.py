# -*- coding: utf-8 -*-
# @CreateTime:  2018/3/1 13:27 
# @CreateBy:    Alvin
# @File:        Zeus.py
# @UpdateTime:
# @UpdateBy:
import getopt
import os
import sys


def usage():
    comm = os.path.basename(sys.argv[0])

    print "Usage: Zeus options \n"
    print "     -d: Domain to search or company name"
    print "     -b: data source: baidu, bing, google, all\n"
    print "     -f: Save the results into an HTML"
    print "     -l: Limit the number of results to work with"
    print "\nExamples:"
    print "     " + comm + " -d qq.com -l 500 -b baidu -f result.html"


def start(argv):
    if len(sys.argv) < 4:
        usage()
        sys.exit()
    try:
        opts, args = getopt.getopt(argv, "l:d:b:s:vf:nhcte:")
    except getopt.GetoptError:
        usage()
        sys.exit()


if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print "Search interrupted by user.."
    except:
        sys.exit()
