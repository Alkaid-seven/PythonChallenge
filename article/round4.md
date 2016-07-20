#PythonChallenge - round 4 

## describe
![alt text][stage_one_img]

[stage_one_img]: ../images/round4


URL http://www.pythonchallenge.com/pc/def/linkedlist.php

```
urllib may help. DON NOT TRY ALL NOTHINGS, since it will never 
end. 400 times is more than enough.
```

本关没有任何的文字提示，开一下source，能够看见以上字符.
并且图片元素外层包裹了一个<a> 标签，有href属性，如下：

```
  <a href="linkedlist.php?nothing=12345">
    <img src="chainsaw.jpg" border="0">
  </a>
```

点击一下图片，会redirect到另一个页面，并持续给出 nothing 的值。
```
and the next nothing is 45439
```

在URL上面替换了 nothing 的值之后，再direct到另一个页面，持续几次之后，会告诉你
```
Your hands are getting tired and the next nothing is 94485
```

按照题意，应该是用urllib这个库，请求400次左右，到最后 nothing 的值会保持不变。
所以关键在于 urllib 的使用。

## answer

```
```

## 题外话之：网络请求

## 题外话之：urllib 库的使用
