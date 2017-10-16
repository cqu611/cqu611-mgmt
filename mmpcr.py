#!/usr/bin/python2.7
# mmpcr - traverse text file and delete the '\r'
# Created by Ekira, 2017/10/16

import sys, os

def func(filename):
    cnt = 0
    cnt_n = 0
    cnt_r = 0
    cnt_rn = 0
    text = []
    with open(filename, "rt") as f:
        for i in f:
            if len(i) > 1 and i[-2:] == '\r\n':
                cnt_rn += 1
                i = i[:-2]
            elif len(i) > 0 and i[-1] == '\r':
                cnt_r += 1
                i = i[:-1]
            elif len(i) > 0 and i[-1] == '\n':
                cnt_n += 1
                i = i[:-1]
            else:
                cnt += 1
            text.append(i)
    print "[REMOVE] CRLF= %d, CR= %d, LF= %d, NOT DEL=%d" % (cnt_rn, cnt_r, cnt_n, cnt)

    with open(filename, 'wt') as f:
        for i in text:
            f.write(i+"\n")
    print "COMPLETED!"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "ERROR VALUE, USAGE: mmpcr [file name]"
        exit()
    if not os.path.isfile(sys.argv[1]):
        print "ERROR VALUE, USAGE: mmpcr [file name]"
        exit()
    func(sys.argv[1])

