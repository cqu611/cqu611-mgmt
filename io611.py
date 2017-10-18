#!/usr/bin/python2.7
# io611 - A simple program to record info of warehouse in and out
# Created by Aran-lq, 2017/10/18
import sys, os, pickle

def func(key, value, flag):
    if os.path.exists('./WareData.pkl'):
        pkl_file = open('WareData.pkl','rb')
        WareHouseData = pickle.load(pkl_file)
    else:
        WareHouseData = {}
    if (flag=='-'):
        tmp = int(WareHouseData[key]) - int(value)
        WareHouseData[key] = str(tmp)
    else:
        if (WareHouseData.has_key(key)):
            tmp = int(WareHouseData[key]) + int(value)
            WareHouseData[key] = str(tmp)
        else:
            WareHouseData[key] = value
    print ("Following are the things in 607:\n")
    for i in range(len(WareHouseData)):
        print (WareHouseData.items()[i])
    output = open('WareData.pkl','wb')
    pickle.dump(WareHouseData, output)
    output.close()
    print "Completed!"

if __name__ == "__main__":
    if (len(sys.argv) != 3) and (len(sys.argv)!=4):
        print "Error value, usage: io607 [key] [value]"
        exit()
    func(sys.argv[1], sys.argv[2], sys.argv[3])
