#!/usr/bin/env python
# encoding: utf-8


def translation(strin):
    resultString = ''
    for i in strin:
        asciiNumber = ord(i)
        if asciiNumber > 96 and asciiNumber < 123:
            asciiNumber = (asciiNumber - 95) % 26 + 97
        else:
            pass
        asciiChar = chr(asciiNumber)
        resultString = resultString + asciiChar
    return str(resultString)

if __name__ == "__main__":
    magicString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    print translation(magicString)
