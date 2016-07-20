#PythonChallenge - round 2

## describe
![alt text][stage_one_img]

[stage_one_img]: ../images/round2


URL http://www.pythonchallenge.com/pc/def/ocr.html

```
recognize the characters. maybe they are in the book, 
but MAYBE they are in the page source.
```

所有的chracters都在网页的source里面。

## answer

```
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

输出：
equality
```

