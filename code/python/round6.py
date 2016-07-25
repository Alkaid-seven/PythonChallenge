#!usr/bin/env python
# encoding: utf-8

import zipfile
import os


def getFileLikeObject():
    currentProjectPath = '/'.join(os.path.abspath('round6.py').split('/')[0:-3])
    zipFilePath = currentProjectPath + '/source/channel.zip'
    return zipfile.ZipFile(zipFilePath, 'r')


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
    return (nextNumber, theComment)


def getNumberFromTxtFile(channelFile, number):
    fileName = number + '.txt'
    fileContent = channelFile.read(fileName)
    theCommentInFile = channelFile.getinfo(fileName).comment
    wordsList = fileContent.split(' ')
    nextNumber = [newNumber for newNumber in wordsList if newNumber.isdigit()]
    if len(nextNumber) == 1:
        return (nextNumber[0], theCommentInFile)
    else:
        return (fileContent, theCommentInFile)


if __name__ == "__main__":
    (fileContent, comments) = getCommentFromFile()
    print 'the answer for stage 6 \n'
    print fileContent
    print ''.join(comments)
    print "SUCCESS"
