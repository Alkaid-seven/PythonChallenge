#!/usr/bin/env python
# encoding: utf-8

import os
import re
import urllib2


# this readFile func need to refactor, for it can't get the abs path for the file when
# run the script not in this folder.
def readFile():
    path = os.path.abspath('./third.txt')
    fileContent = open(path, 'r').read()
    return fileContent


def getResponse():
    try:
        f = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
        content = f.read()
    except urllib2.URLError, e:
        content = e.code
    return content


def findLowercase(characters):
    lowercseList = re.findall('[^A-Z][A-Z]{3}([a-z]){1}[A-Z]{3}[^A-Z]', characters)
    return lowercseList


if __name__ == "__main__":
    # charactersByReadFile = readFile()
    charactersByRespone = getResponse()
    lowercseList = findLowercase(charactersByRespone)
    print ''.join(lowercseList)
