#PythonChallenge - round 5

## describe
![alt text][stage_one_img]

[stage_one_img]: ../images/

URL:

```
in fo in the page
```

thinking

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
