#PythonChallenge - round 6

## describe
![alt text][stage_one_img]

[stage_one_img]: ../images/round6

URL: http://www.pythonchallenge.com/pc/def/channel.html

```
PayPal button fot Donate
```
查看 source 文件，有一段话，希望我们给 PythonChallenge 捐助。

```
The following has nothing to do with the riddle itself. I just
thought it would be the right point to offer you to donate to the
Python Challenge project. Any amount will be greatly appreciated.

-thesamet

```
在 head 上面有一个提示

```
<!-- <-- zip -->
```
 感觉跟 zip 有关的样子。
 尝试将 URL 后面的 channel.html 换成 zip.html，出现一下的文字

 ```
 yes. find the zip.
 ```
 尝试将 URL 后面的 .html 换成 .zip
 可以下载下来一个zip文件。解压之后全是txt文件，其中有一个是readme


## 题外话之: 文件压缩

## 题外话之: zipfile 模块
zipfile模块用来做zip格式编码的压缩和解压缩的

### zipfile 常用方法

- zipfile.ZipFile(file[, mode[, compression[, allowZip64]]]) : 创建一个ZipFile对象，表示一个zip文件
file: 文件的路径或类文件对象(file-like object)
mode: 打开zip文件的模式
      'r' 表示读已经存在的zip文件
      'w' 表示新建一个只写的zip文档或覆盖一个已经存在的只写的zip文档
      'a' 表示将数据附加到一个现存的zip文档中
compression: 表示压缩格式，可选的压缩格式只有2个
      ZIP_STORE: 默认的，表示不压缩；
      ZIP_DEFLATED: 表示压缩，
allowZip64: 为True时，表示支持64位的压缩，当在所压缩的文件大于2G时，会用到这个选项，默认情况下，该值为False，因为Unix系统不支持。

- zipfile.write(filename[, arcname[, compress_type]]) : 讲指定文件添加到zip文档中
fileName: 文件路径
acrname: 添加到zip文档之后保存的名称
compress_type:  表示压缩方法。 ZIP_STORED 或 ZIP_DEFLATED

- zipFile.extract(member[, path[, pwd]]): 将zip文档内的指定文件解压到当前目录
member : 要解压的文件名称或对应的ZipInfo对象
path : 解析文件保存的路径
pwd : 解压密码
