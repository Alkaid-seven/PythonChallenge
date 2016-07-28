#PythonChallenge - round 5

## describe
![alt text][stage_one_img]

[stage_one_img]: ../images/round8

URL: http://www.pythonchallenge.com/pc/def/integrity.html

```
Where is the missing link?
```

首先查看源代码，得到两个信息：

1. map beside the img element

```
<map name="notinsect">
	<area shape="poly"
coords="179,284,214,311,255,320,281,226,319,224,363,309,339,222,371,225,411,229,404,242,415,252,428,233,428,214,394,207,383,205,390,195,423,192,439,193,442,209,440,215,450,221,457,226,469,202,475,187,494,188,494,169,498,147,491,121,477,136,481,96,471,94,458,98,444,91,420,87,405,92,391,88,376,82,350,79,330,82,314,85,305,90,299,96,290,103,276,110,262,114,225,123,212,125,185,133,138,144,118,160,97,168,87,176,110,180,145,176,153,176,150,182,137,190,126,194,121,198,126,203,151,205,160,195,168,217,169,234,170,260,174,282" 
	href="../return/good.html">
</map>
```
2. username and password

```
<!--
un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
-->
```



## answer
```
#!usr/bin/env python
# encoding: utf-8



输出:

```


## 题外话之: 主要闯关tech


## 题外话之:  main 库的使用


### main pickle 常用方法

example
详细用法: http://www.cnblogs.com/cobbliu/archive/2012/09/04/2670178.html

- pickle.dump(obj, file, [,protocol]) : 将对象obj保存到文件file中去
protocol: 序列化使用的协议版本
file: 对象保存到的类文件对象

- pickle.load(file) : 从file中读取一个字符串，并将它重构为原来的python对象。
file: 类文件对象，有read()和readline()接口。
