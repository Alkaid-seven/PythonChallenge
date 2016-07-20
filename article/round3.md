#PythonChallenge - round 3

## describe
![alt text][stage_one_img]

[stage_one_img]: ../images/round3


URL http://www.pythonchallenge.com/pc/def/equality.html

```
One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
```

source code 里面有一大堆的字母，跟前一关一样。

根据提示，本关是找出左右各有3个大写字母围绕的中间的小写字母。

## answer

```
#!/usr/bin/env python
# encoding: utf-8

import os
import re
import urllib2


def getResponse():
    try:
        f = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
        content = f.read()
    except urllib2.URLError, e:
        content = e.code
    return content


def findLowercase(characters):
    lowercseList = re.findall('[^A-Z][A-Z]{3}([a-z]){1}[A-Z]{3}[^A-Z]', characters)
    return lowercseList


if __name__ == "__main__":
    charactersByRespone = getResponse()
    lowercseList = findLowercase(charactersByRespone)
    print ''.join(lowercseList)

输出:
linkedlist

```

## 题外话之：正则表达式

```
字符串是编程时涉及到的最多的一种数据结构，对字符串进行操作的需求几乎无处不在。比如判断一个字符串
是否是合法的Email地址，虽然可以编程提取@前后的子串，再分别判断是否是单词和域名，但这样做不但麻
烦，而且代码难以复用。

正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串定义一个
规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。

所以我们判断一个字符串是否是合法的Email的方法是：

创建一个匹配Email的正则表达式；

用该正则表达式去匹配用户的输入来判断是否合法。

因为正则表达式也是用字符串表示的，所以，我们要首先了解如何用字符来描述字符。
																	------廖雪峰
```
```\d``` 可以匹配一个数字

```\w``` 可以匹配一个字母或数字

```\s``` 可以匹配一个空格（也包括Tab等空白符）

```.``` 可以匹配任意字符，所以：'py.'可以匹配'pyc'、'pyo'、'py!'

```*``` 表示任意个字符（包括0个）

```+``` 表示至少一个字符

```?``` 表示0个或1个字符

```{n}``` 表示n个字符

```{n,m}``` 表示n-m个字符

```\``` 用于转义特殊字符: '_' 等

```[0-9a-zA-Z\_]``` 可以匹配一个数字、字母或者下划线；

```[0-9a-zA-Z\_]+``` 可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

```[a-zA-Z\_][0-9a-zA-Z\_]*``` 可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

```[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}``` 更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

```A|B``` 可以匹配A或B，所以[P|p]ython可以匹配'Python'或者'python'。

```^``` 表示行的开头，```^\d``` 表示必须以数字开头。

```$``` 表示行的结束，```\d$``` 表示必须以数字结束。
