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

        parser_group_target = parser.add_argument_group("Target Specification")
        parser_group_target.add_argument("-d", dest="domain", help="Domain to search or company name")
        parser_group_target.add_argument("-iF", dest="inputfile", help="input file that has an domain/company list")

        parser_group_domain = parser.add_argument_group("Subdomain Dciscovery")
        parser_group_domain.add_argument("-b", dest="domain", help="Domain to search or company name")
        parser_group_domain.add_argument("-iF", dest="inputfile", help="input file that has an domain/company list")

        args = parser.parse_args()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    start()
