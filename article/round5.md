#PythonChallenge - round 5

## describe
![alt text][stage_one_img]

[stage_one_img]: ../images/round5

URL: http://www.pythonchallenge.com/pc/def/peak.html

```
pronounce it 
```

按照之前的思路，试一试打开 source 文件，查看源码
```
<peakhell src="banner.p">
  <!-- peak hell sounds familiar ? -->
</peakhell>
```

首先，先把URL中 ```peak.html``` 替换成 ```banner.p```， 能够看到一些字符
在看第二个线索：```peak hell sounds familiar``` ，应该指的是 ```pickle``` 库


## answer
```
#!usr/bin/env python
# encoding: utf-8

import urllib
import pickle


def readDataFromFile():
    openFile = file('../../source/banner.p', 'r')
    return openFile


if __name__ == "__main__":
    pickledDataFromFile = readDataFromFile()
    unpickerData = pickle.load(pickledDataFromFile)
    finalObject = []
    for lineList in unpickerData:
        line = [ch * count for ch, count in lineList]
        print "".join(line)


输出:
channel
```

## 题外话之: 数据对象持久化操作

持久性的基本思想很简单。假定有一个 Python 程序，它可能是一个管理日常待办事项的程序，您希望在多次执行这个程序之间可以保存应用程序对象（待办事项）。换句话说，您希望将对象存储在磁盘上，便于以后检索。这就是持久性。要达到这个目的，有几种方法，每一种方法都有其优缺点。
例如，可以将对象数据存储在某种格式的文本文件中，譬如 CSV 文件。或者可以用关系数据库，譬如 Gadfly、MySQL、PostgreSQL 或者 DB2。这些文件格式和数据库都非常优秀，对于所有这些存储机制，Python 都有健壮的接口。
这些存储机制都有一个共同点：存储的数据是独立于对这些数据进行操作的对象和程序。这样做的好处是，数据可以作为共享的资源，供其它应用程序使用。缺点是，用这种方式，可以允许其它程序访问对象的数据，这违背了面向对象的封装性原则 — 即对象的数据只能通过这个对象自身的公共（public）接口来访问。
如果希望透明地存储 Python 对象，而不丢失其身份和类型等信息，则需要某种形式的对象序列化：它是一个将任意复杂的对象转成对象的文本或二进制表示的过程。同样，必须能够将对象经过序列化后的形式恢复到原有的对象。
在 Python 中，这种序列化过程称为 pickle，可以将对象 pickle 成字符串、磁盘上的文件或者任何类似于文件的对象，也可以将这些字符串、文件或任何类似于文件的对象 unpickle 成原来的对象。


## 题外话之: pickle 库的使用
pickle 库实现了基本的数据序列和反序列化。
通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储
通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

### pickle 常用方法

详细用法: http://www.cnblogs.com/cobbliu/archive/2012/09/04/2670178.html

- pickle.dump(obj, file, [,protocol]) : 将对象obj保存到文件file中去
protocol: 序列化使用的协议版本
          0：ASCII协议，所序列化的对象使用可打印的ASCII码表示
          1：老式的二进制协议
          2：2.3版本引入的新二进制协议，较以前的更高效
          其中协议0和1兼容老版本的python。protocol默认值为0
file: 对象保存到的类文件对象
      file必须有write()接口, file可以是一个以'w'方式打开的文件或者一个StringIO对象或者其他任何实现write()接口的对象。如果protocol>=1，文件对象需要是二进制模式打开的

- pickle.load(file) : 从file中读取一个字符串，并将它重构为原来的python对象。
file: 类文件对象，有read()和readline()接口。

dump() 函数能一个接着一个地将几个对象转储到同一个文件
随后调用 load() 来以同样的顺序检索这些对象
可移植性: 空间和时间上说，pickle 是可移植的。pickle 文件格式独立于机器的体系结构，在 Linux 下创建一个 pickle，可将它发送到在 Windows 或 Mac OS 下运行的 Python 程序。
