#! usr/bin/env python
import re
import urllib2


def Searchchar(str):
    result = re.findall('[^A-Z][A-Z]{3}([a-z]){1}[A-Z]{3}[^A-Z]',str)
    return result


if __name__ == "__main__":
    try:
        f = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
        content = f.read()
    except urllib2.URLError,e:
        content =  e.code
        print content
    else:
        result = Searchchar(content)
        print ''.join(result)
    finally:
        print '-'*50
