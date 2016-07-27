#PythonChallenge - rund 7


## describe
![alt text][stage_one_img]

[stage_one_img]: ../images/round7

URL: http://www.pythonchallenge.com/pc/def/oxygen.html

图像有点奇怪，但是页面什么提示也没有，源文件也没有提示。
猜想可能跟那个灰黑色的横条有关。

但是没有找到可以自动获取图片中的灰黑色横条的方法。网上搜索了一下，找到了一个个人比较喜欢的解决方案：
先用pillow将图片解析，获取图片中间高度的RGB值
其次间隔七个过滤出RGB值，对应ACSCII码解析
然后得到一个list，将其连接起来如下：
smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
再解析最后一组数据，连接输出
integrity

## answer

```
#!/usr/bin/env python
# encoding: utf-8


import re
import requests
from io import BytesIO
from PIL import Image


if __name__ == "__main__":
    imgInStage7 = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))
    row = [imgInStage7.getpixel((x, imgInStage7.height / 2)) for x in range(imgInStage7.width)][::7]
    ords = [r for r, g, b, a in row if r == g == b]
    nums = re.findall("\d+", "".join(map(chr, ords)))
    print "".join(map(chr, map(int, nums)))

输出:
integrity

```

## 题外话之：图像处理

## 题外话之：pillow 库