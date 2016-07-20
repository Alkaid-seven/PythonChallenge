#!/usr/bin/env python
# encoding: utf-8 

import urllib
import re


def getTheDataFromURL(url):
  dataFromURL = urllib.urlopen(url).read()
  return dataFromURL


def joinTheNewURL(newID):
  THE_BASE_URL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' 
  theNewURL = THE_BASE_URL + str(newID)
  return theNewURL


def matchNewIDByRegex(newData):
  # 这样不make sense，应该有其他的更好的匹配规则
  newIDlist = re.findall('\d{4,5}', newData)
  print newIDlist
  return newIDlist[0]


def try400Times():
  # need to refactor
  initialIDList = [12345, 3875, 160]
  initialID = 56828
  allTheID = []
  for i in range(0, 400):
    print i
    if initialID not in allTheID:
      allTheID.append(initialID)
      newURL = joinTheNewURL(initialID)
      print newURL
      newData = getTheDataFromURL(newURL)
      print newData
      initialID = matchNewIDByRegex(newData)
      print initialID

    else:
      print initialID
      print allTheID
      theLocationOfID = allTheID.index(initialID)
      initialID = allTheID[theLocationOfID+1]

  print initialID


if __name__ == "__main__":
  try400Times()
  print 'a'
