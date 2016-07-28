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

## 题外话之: HTML map & area 标签
首先，html 的 map 标签中。

area 元素永远嵌套在 map 元素内部。area 元素可定义图像映射中的区域。 
img 元素中的 usemap 属性可引用 <map> 中的 id 或 name 属性（取决于浏览器），所以我们应同时向 <map> 添加 id 和 name 属性。

Map 对象集合

areas: 返回 image-map 中所有 <area> 元素的集合。
images: 返回与 image-map 相关联的所有 <img> 和 <object> 元素的集合。

Map 对象属性
name: 设置或返回 image-map 的 name 属性值。

其次，htlm 中的 area 标签。

<area> 标签定义图像映射中的区域（注：图像映射指得是带有可点击区域的图像）。

coords 属性与 shape 属性配合使用，来规定区域的尺寸、形状和位置。

shape 属性

shape 属性的值会影响浏览器对 coords 属性的解释。如果未使用 shape 属性，那么会假设使用值 default。依照标准，default 意味着该区域覆盖整个图像。在实际中，浏览器默认使用矩形区域，并期望能找到 4 个 coords 值。如果没有指定形状，而且在标签中也没有包括 4 个坐标，那么浏览器会忽略整个区域。
default	规定全部区域。
rect	定义矩形区域。
circ	定义圆形。
poly	定义多边形区域。

coords 属性

coords 属性定义了客户端图像映射中对鼠标敏感的区域的坐标。坐标的数字及其含义取决于 shape 属性中决定的区域形状。可以将客户端图像映射中的超链接区域定义为矩形、圆形或多边形等。

x1,y1,x2,y2	如果 shape 属性设置为 "rect"，则该值规定矩形左上角和右下角的坐标。
x,y,radius	如果 shape 属性设置为 "circ"，则该值规定圆心的坐标和半径。
x1,y1,x2,y2,..,xn,yn	如果 shape 属性设置为 "poly"，则该值规定多边形各边的坐标。如果第一个坐标和最后一个坐标不一致，那么为了关闭多边形，浏览器必须添加最后一对坐标。



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
