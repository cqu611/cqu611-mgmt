#!/bin/python2.7

import re, os


def mmpcmt(path):
    regex = "\/\*[\s\S]*\*\/|\/\/.*"
    reobj = re.compile(regex)
    txt = []
    with open(path, 'rt') as f:
        for i in f:
            rst, cnt = reobj.subn("", i)
            txt.append(rst)
    with open(path, 'wt') as f:
        for i in txt:
            f.write(i)
    print "Completed!"


if __name__ == '__main__':
    mmpcmt("ufs.h")


