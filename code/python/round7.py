#!/usr/bin/env python
# encoding: utf-8


import re
import requests
from io import BytesIO
from PIL import Image

# the code is coming form https://hackingnote.gitbooks.io/the-python-challenge-solutions/content/level-7.html
# I think it is concise and I like it very much
# let me thinking about: we need the concise code or the readable code.


def readFromJPG():
    imgInStage7 = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))
    row = [imgInStage7.getpixel((x, imgInStage7.height / 2)) for x in range(imgInStage7.width)][::7]
    ords = [r for r, g, b, a in row if r == g == b]
    nums = re.findall("\d+", "".join(map(chr, ords)))
    return "".join(map(chr, map(int, nums)))


if __name__ == "__main__":
    print 'the answer fot Stage 7 is: \n'
    print readFromJPG()
    print 'SUCCESS'
