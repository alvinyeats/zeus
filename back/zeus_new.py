# -*- coding: utf-8 -*-
# @CreateTime:  2018/3/1 13:27
# @CreateBy:    Alvin
# @File:        Zeus.py
# @UpdateTime:
# @UpdateBy:

import argparse
import queue


def start():
    target_queue = queue.Queue()

    try:
        parser = argparse.ArgumentParser(description="zeus args parser")

        parser_group_target = parser.add_argument_group("Target Specification")
        parser_group_target.add_argument("-d", dest="domain", nargs="+", help="Domain to searches or company name")
        parser_group_target.add_argument("-if", dest="inputfile", nargs="?", help="input file that has an domain/company list")

        parser_group_domain = parser.add_argument_group("Subdomain Dciscovery")
        parser_group_domain.add_argument("-s", dest="searchengine", nargs="?", help="Search engine to use")
        parser_group_domain.add_argument("-st", dest="searches thread", nargs="?", help="Search thread")

        args = parser.parse_args()
        print(args)

        # add args
        if args.domain:
            for d in args.domain:
                target_queue.put(d)
        elif args.inputfile:
            with open(args.inputfile) as f:
                for line in f.readlines():
                    target_queue.put(line.strip())

        # start searches sub domain
        while not target_queue.empty():
            print(target_queue.get())



    except Exception as e:
        print(e)


if __name__ == "__main__":
    start()
