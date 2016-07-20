#! usr/bin/env python
import math
import string

def translation(strin):
    end = ''
    for i in strin:
        n = ord(i)
        if n > 96 and n < 123:
            n = (n-95)% 26 + 97
        else:
            n = n
        m = chr( n )
        end = end + m
    return str(end)
if __name__ == "__main__":
    #start = "http://www.pythonchallenge.com/pc/def/map.html" jvvr://yyy.ravjqpejanngpig.eqo/re/fgh/oar.jvon
    start = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    #using string.maketrans() is reaommended. now apply on the url.
   # start = "map"
    print translation(start)