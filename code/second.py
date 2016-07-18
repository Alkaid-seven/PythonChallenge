#! usr/bin/env python
import os
import sys

def findfile():
    path = os.path.abspath('second.txt')
    thefile = open(path,'r')
    content = thefile.read()
    thefile.close()
    return content

def count(thestr):
    countor = {'string':'num'}
    for i in thestr:
        if i in countor.keys():
            countor[i] +=1
        else:
            countor[i] = 1
    return countor
def count2(thestr):

    pass
def lesschar2(chardict):
   # num = chardict[j] for j in chardict.keys()
    pass
def lesschar(chardict,content):
    i = len(content)
    for n in range(len(chardict)):
        if i > n :
            i = n
        else:
            pass
    print i
    endstr = [n for n in chardict.keys() if chardict[n] == 1]
    return endstr


if __name__ == "__main__":
    content = findfile()
    chardict =  count(content)
    result = lesschar(chardict,content)
    print ''.join(result)