#!/usr/bin/env python
# encoding: utf-8

import urllib


def getTheDataFromURL(url):
    dataFromURL = urllib.urlopen(url).read()
    return dataFromURL


def joinTheNewURL(newID):
    THE_BASE_URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    theNewURL = THE_BASE_URL + str(newID)
    return theNewURL


def matchNewIDByRegex(newData):
    wordList = newData.split(' ')
    digitList = [word for word in wordList if word.isdigit()]
    if len(digitList) > 0:
        newID = digitList[0]
    else:
        newID = wordList[0]
    return newID


def try400Times():
    initialID = 12345
    for i in range(0, 400):
        print '%d: %s' % (i, initialID)
        newURL = joinTheNewURL(initialID)
        newData = getTheDataFromURL(newURL)
        if newData.startswith('Yes'):
            initialID = str(int(initialID) / 2)
            continue
        initialID = matchNewIDByRegex(newData)
        if not initialID.isdigit():
            break
    print initialID


if __name__ == "__main__":
    try400Times()
