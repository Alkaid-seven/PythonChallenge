#!usr/bin/env python
# encoding: utf-8

import urllib
import pickle

def getTheDataFromURL():
    URL = "http://www.pythonchallenge.com/pc/def/banner.p"
    return urllib.urlopen(URL).read()

def readDataFromFile():
    openFile = file('../../source/banner.p', 'r')
    return openFile


if __name__ == "__main__":
#    thePickledData = getTheDataFromURL()
    pickledDataFromFile = readDataFromFile()
    unpickerData = pickle.load(pickledDataFromFile)
    finalObject = []
    for lineList in unpickerData:
#        print lineList
        line = [ch * count for ch, count in lineList]
        finalObject.append("".join(line))

    for eachLine in finalObject:
        print eachLine
