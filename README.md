# dataHelper

An useful data helper

> updatetime 2019/02/28/ 01:08

统一数据格式：

`id,content,aspect,sentimentword,polarity`

#### removeinvalidlines.py

用来移除文件中的无效行，执行时会提示输入两个字符串，第一个要求输入待处理文件名称（或相对/绝对路径），第二个要求输入输出文件名称（或相对/绝对路径），运行结束后，会生成一个处理后的文件，并且会在控制台输出当前总的有效行数。

#### conflicthandling.py

用来比较两个不同文件的差异，执行时要求输入两个字符串，分别为两个待处理文件名（或相对/绝对路径）。处理完成后，会在控制台输出两个文件冲突发生的位置，同时也会在文件目录下生成一个ConflictInfo.csv文件来记录两个文件冲突之处。同时请注意，在使用该文件时，请确定两个待处理文件的前两列完全一致（即id和content），排序也要完全一样！

#### dataHelper.py

该文件有三种用途:1.将错误的中文分号改为英文分号   2.将多打的英文分号删除   3.将字符串中间的分隔符转化为分号;
针对第三点用途的补充：以后在写入词组的时候，不再需要频繁切换中英文来输入英文分号，只需要在要分隔的地方打上任意个符号(符号种类目前支持四种，分别为空格、英文分号、中文分号和你输入的自定义符号，这四种符号既可以分开用，也可以混合在一起用)，最后在程序运行时输入分隔时所用的自定义符号，则脚本可以将分隔符改为英文分号.
```
请输入想要替换成英文分号的字符:--->输入符号后，程序将会把分隔符改为英文分号
```

#### marker.py

与 marksplit 配合使用。给未打上任何 mark 的已标记行打上 mark ，用于标记当天的工作。第二天可以在第一天的输出文件上继续工作。使用第六列，index 为 5 ，作为 mark 列。
```
Usage:
  marker <src> <out> <tag> <encode>
```
例：
```
python marker.py input.csv out.csv tag1 gbk
# or
python marker.py input.csv out.csv tag1 utf-8
# 输出文件：out.csv
```

#### marksplit.py

与 marker 配合使用。从打上 mark 的csv文件中分离出相应的 mark 行，输出到文件，并删除 mark 。结果可在其他处理后提交。
```
Usage:
  marksplit <src> <mark> <item> <encode>
```
例：
```
python marksplit.py out.csv tag1 衣服 gbk
# 输出文件： 衣服-XX-YYYYmmdd.csv
```
输出文件名自动设置为`item-有效行数-日期.csv`。

另外：

1. 请使用`python3`运行本文件。
2. 若编码错误，例：（`UnicodeDecodeError: 'gbk' codec can't decode byte 0xa2 in position 50:      illegal multibyte sequence"`）这是由于python读写文件时默认以ansi方式读写，请检查您的文件编码，尝试改为ansi编码再运行。
3. 命令行下可用 Tab 补全文件名。
