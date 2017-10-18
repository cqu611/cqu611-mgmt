#!/bin/python2.7

import re, os

def find_text(f, kw):
    text = list()
    with open(f, "rt") as fp:
        for i in fp:
            if kw in i:
                print i


def main(DIR, KEY):
    pathes = os.listdir(DIR)
    for i in pathes:
        i = DIR + "/" + i
        if os.path.isfile(i):
            find_text(i, KEY)
        elif os.path.isdir(i):
            main(i, KEY)



if __name__ == "__main__":
    DIR = "lightnvm"
    KEY = "trace"
    main(DIR, KEY)