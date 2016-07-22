#!usr/bin/env python
# encoding: utf-8

import zipfile


def getFileLikeObject():
    filePath = '/Users/jfliu/Code/Python/PythonChallenge/source/channel.zip'
    return zipfile.ZipFile(filePath, 'r')


def printInfo():
    channelFile = getFileLikeObject()
    return channelFile.comment


def getDataFromZipFile():
    channelFile = getFileLikeObject()
    startFileName = '90052'
    nextNumber = getNumberFromTxtFile(channelFile, startFileName)
    while nextNumber.isdigit():
        nextNumber = getNumberFromTxtFile(channelFile, nextNumber)
    return nextNumber


def getCommentFromFile():
    theComment = []
    channelFile = getFileLikeObject()
    (nextNumber, comment) = getNumberFromTxtFile(channelFile, '90052')
    theComment.append(comment)
    while nextNumber.isdigit():
        (nextNumber, comment) = getNumberFromTxtFile(channelFile, nextNumber)
        theComment.append(comment)
    return theComment


def getNumberFromTxtFile(channelFile, number):
    fileName = number + '.txt'
    fileContent = channelFile.read(fileName)
    print fileName
    print fileContent
    theCommentInFile = channelFile.getinfo(fileName).comment
    wordsList = fileContent.split(' ')
    nextNumber = [number for number in wordsList if number.isdigit()]
    if len(nextNumber) == 1:
        return (nextNumber[0], theCommentInFile)
    else:
        return (fileContent, theCommentInFile)


if __name__ == "__main__":
#    import pdb;pdb.set_trace()
#    theInfo= getDataFromZipFile()
    result = getCommentFromFile()
#    print printInfo()
#    print theInfo
    print ''.join(result)
    print "SUCCESS"
