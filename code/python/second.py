#! usr/bin/env Python

import os
import sys

def filefind():
    path = os.path.abspath('second.txt')
    thefile = open(path,'r')
    content = thefile.read()
    thefile.close()
    return content

def count(str):
    arry = []
    thestr = []
    for i in str:
        if i in thestr:
            n = thestr.index(i)
            arry[n][1] += 1
        else:
            thestr.append(i)
            arry.append([i,1])
    return arry

def theless(arry):
    j = len(arry)
    endstr = []
    for k in arry:
        if j >= k[1]:
            j = k[1]
        else:
            pass
    for i in arry:
        if i[1] == j:
            endstr.append(i[0])
        else:
            pass
    return endstr

if __name__ == "__main__":
    content = filefind()
    arry = count(content)
    result = theless(arry)
    print ''.join(result)