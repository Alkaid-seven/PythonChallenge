# PythonChallenge －round 1	
## describe
![alt text][stage_one_img]

[stage_one_img]: /Users/jfliu/Documents/pythonChallenge/images/round1


URL http://www.pythonchallenge.com/pc/def/274877906944.html

```
everybody thinks twice before solving this.

g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
```

## answer

```
#! usr/bin/env Python
import math
import string


def translation(strin):
    end = ''
    for i in strin:
        n = ord(i)
        if n > 96 and n < 123:
            n = (n-95)% 26 + 97
        else:
            pass
        m = chr( n )
        end = end + m
    return str(end)


if __name__ == "__main__":
    start = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    print translation(start)
    
输出：
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url. 
```
I
