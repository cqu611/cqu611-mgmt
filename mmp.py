#! /bin/python2.7
# -*- coding: utf-8 -*-
#
# mmp - several tools.
#
# @Xiong X. 2017/10/20

import sys

def usage(args):
    print("""\
usage: mmp [version] [help] [<command> [<args>]]\n
There are common MMP commands used in various situations:\n
    rename      rename file(s) or directory(s) in FORMAT
    comment     remove comment from file(s) or directory(s)
    cr          remove cr ('\\r') from file(s) or directory(s)
    keyword     search keyword from file(s) or directory(s)
    version     print current mmp version
    help        print manual text""")


def version(args):
    print("MMP version 0.0.1")


def mmp_rename(args):
    print("rename")


def mmp_comment(args):
    print("comment")


def mmp_cr(args):
    print("cr")


def mmp_keyword(args):
    print("keyword")


def parse_command(cmd):
    cmdlen = len(cmd)
    if cmdlen == 0:
        return None
    elif cmd == "help"[:cmdlen]:
        return usage
    elif cmdlen > 1 and cmd == "comment"[:cmdlen]:
        return mmp_comment
    elif cmd == "cr":
        return mmp_cr
    elif cmd == "rename"[:cmdlen]:
        return mmp_rename
    elif cmd == "keyword"[:cmdlen]:
        return mmp_keyword
    elif cmd == "version"[:cmdlen]:
        return version
    else:
        return None


if __name__ == "__main__":
    args = sys.argv
    if (len(args) == 1):
        usage(None)
        exit()
    cmd_fn = parse_command(args[1])
    if cmd_fn == None:          ## Can not parse command
        usage(None)
        exit()
    ret = cmd_fn(args[2:])
    if ret == 0:                ## run command successful
        exit()
    # TODO: Handle error for command