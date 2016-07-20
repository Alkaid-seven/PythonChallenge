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

urllib模块提供的上层接口，使我们可以像读取本地文件一样读取www和ftp上的数据。

### urllib 常用方法

- urllib.urlopen(url[, data[, proxies]]) : urlopen方通过url获取法远程数据，并创建一个类文件对象，然后像操作本地文件一样操作这个类文件对象(远程数据)
url：远程数据的地址，一般就是网址
data：表示以post方式提交到url的数据
proxies：用于设置代理

urlopen() 会返回一个类文件对象
* read() , readline() , readlines() , fileno() , close() ：这些方法的使用方式与文件对象完全一样;
* info()：返回一个httplib.HTTPMessage 对象，表示远程服务器返回的头信息；
* getcode()：返回Http状态码。如果是http请求，200表示请求成功完成;404表示网址未找到；
* geturl()：返回请求的url；

- urllib.urlretrieve(url[, filename[, reporthook[, data]]]) : urlretrieve方法直接将远程数据下载到本地
url：远程数据的地址，一般就是网址
filename：指定了保存到本地的路径（如果未指定该参数，urllib会生成一个临时文件来保存数据）
reporthook：是一个回调函数，当连接上服务器、以及相应的数据块传输完毕的时候会触发该回调。我们可以利用这个回调函数来显示当前的下载进度
data：指post到服务器的数据。

urlretrieve() 该方法返回一个包含两个元素的元组(filename, headers)，filename表示保存到本地的路径，header表示服务器的响应头。

- urllib中还提供了一些辅助方法，用于对url进行编码、解码。
url中是不能出现一些特殊的符号的，有些符号有特殊的用途。当以get方式提交数据的时候，会在url中添加key=value这样的字符串，所以在value中是不允许有'='，因此要对其进行编码；
与此同时服务器接收到这些参数的时候，要进行解码，还原成原始的数据。这个时候，这些辅助方法会很有用：
* urllib.quote(string[, safe])：对字符串进行编码。参数safe指定了不需要编码的字符;
* urllib.unquote(string) ：对字符串进行解码；
* urllib.quote_plus(string [ , safe ] ) ：与urllib.quote类似，但这个方法用'+'来替换' '，而quote用'%20'来代替' '
* urllib.unquote_plus(string ) ：对字符串进行解码；
* urllib.urlencode(query[, doseq])：将dict或者包含两个元素的元组列表转换成url参数。例如 字典{'name': 'dark-bull', 'age': 200}将被转换为"name=dark-bull&age=200"
* urllib.pathname2url(path)：将本地路径转换成url路径；
* urllib.url2pathname(path)：将url路径转换成本地路径；

### urllib & urllib2 的区别

>urllib2 can accept a Request object to set the headers for a URL request,urllib accepts only a URL. That means, you cannot masquerade your User Agent string etc. 
>urllib2可以接受一个Request类的实例来设置URL请求的headers，urllib仅可以接受URL。这意味着，你不可以伪装你的User Agent字符串等。
>
>urllib provides the urlencode method which is used for the generation of GET query strings, urllib2 does not have such a function. This is one of the reasons why urllib is often used along with urllib2.
>urllib提供urlencode方法用来GET查询字符串的产生，而urllib2没有。这是为何urllib常和urllib2一起使用的原因。
