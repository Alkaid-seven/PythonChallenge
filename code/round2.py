#!/usr/bin/env python
# encoding: utf-8

import os


def readFile():
    path = os.path.abspath('second.txt')
    fileContent = open(path, 'r').read()
    return fileContent


def countByDic(characters):
    charDict = {}
    for specialChar in characters:
        if (specialChar in charDict.viewkeys()):
            charDict[specialChar] += 1
        else:
            charDict[specialChar] = 1
    return charDict


def countByArray(characters):
    charArray = []
    countedArray = []
    for specialChar in characters:
        if(specialChar in countedArray):
            specialCharLocation = countedArray.index(specialChar)
            charArray[specialCharLocation][1] += 1
        else:
            countedArray.append(specialChar)
            charArray.append([specialChar, 1])
    return charArray


def binarySortArray(charArray):
    j = len(charArray)
    endstr = []
    for k in charArray:
        if j >= k[1]:
            j = k[1]
        else:
            pass
    for i in charArray:
        if i[1] == j:
            endstr.append(i[0])
        else:
            pass
    return endstr


if __name__ == "__main__":
    characters = readFile()
    characterAndNumberDic = countByDic(characters)
    charArrayAndNumberArray = countByArray(characters)
    result = binarySortArray(charArrayAndNumberArray)
    print ''.join(result)
#    print(characterAndNumberDic.viewkeys())
#    print(characterAndNumberDic.viewvalues())
