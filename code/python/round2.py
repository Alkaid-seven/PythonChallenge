#!/usr/bin/env python
# encoding: utf-8


def readFile():
    path = '../source/second.txt'
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


def getValueEqualOneArray(charArray):
    endstr = []
    for eachChar in charArray:
        if eachChar[1] == 1:
            endstr.append(eachChar[0])
        else:
            pass
    return endstr


if __name__ == "__main__":
    characters = readFile()
    characterAndNumberDic = countByDic(characters)
    charArrayAndNumberArray = countByArray(characters)
    result = getValueEqualOneArray(charArrayAndNumberArray)
    print ''.join(result)
#    print(characterAndNumberDic.viewkeys())
#    print(characterAndNumberDic.viewvalues())
