# -*- coding: utf-8 -*-
# @CreateTime:  2018/3/1 13:27
# @CreateBy:    Alvin
# @File:        Zeus.py
# @UpdateTime:
# @UpdateBy:

import argparse


def start():
    try:
        parser = argparse.ArgumentParser(description="zeus args parser")

        parser_group_collect = parser.add_argument_group("Collect")
        parser_group_collect.add_argument("-d", "--domain", dest="domain", help="Domain to search or company name")
        parser_group_collect.add_argument("-if", "--inputfile", dest="inputfile", help="input file that has an domain/company list")

        args = parser.parse_args()
        print(args)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    start()
