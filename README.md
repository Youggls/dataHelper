# dataHelper

An useful data helper

> updatetime 2019/02/28/ 01:08

统一数据格式：

`id,content,aspect,sentimentword,polarity`

#### removeinvalidlines.py

用来移除文件中的无效行，执行时会提示输入两个字符串，第一个要求输入待处理文件名称（或相对/绝对路径），第二个要求输入输出文件名称（或相对/绝对路径），运行结束后，会生成一个处理后的文件，并且会在控制台输出当前总的有效行数。

#### merge.py
用来比较两个文件的冲突，合并
```
Usage:
  merge <file1> <file2> <outputname>
```
或
```
Usage:
  merge <file1> <file2>
```

传入两个文件的名字（路径），第三个参数可缺省，若不传入第三个参数默认在脚本目录下生成out.csv文件
该命令会将两个文件中的第三四五列(Aspect，sentiment_word，polarity)进行分析比较。

无论如何，在输出文件的三、四、五列会写入第一个文件的三、四、五列，在输出文件的六、七、八列会写入第二个文件的三、四、五列。

1.若两个文件的某一行的标注完全一样，会写在输出文件的九、十、十一列写入输入文件的三四五列，在第十二列写入1来标记改行不用再次判断。

2.若两个文件的某一行中标注不完全一致，会在输出文件的九、十、十一列写入输入文件中相同的部分，并且在十二列写入0来标记需要再次判断。

![image](https://github.com/Youggls/pages/blob/master/Snipaste_2019-03-10_01-33-36.png)

如这张图片，第一行的三、四、五列（第一个人标注结果）于第一行六、七、八列出现了区别，在十二列标注0

注意！！！
1.运行前，请将两文件在content那一列上按照降序排列，并确保两个文件对于每一行的content完全一样。

2.若运行中突然退出并且提示```[INFO]: WANINGS! The length of info in file1 is different at line xxx```，请检查您的第一（第二）个文件中的第xxx行是否标注正确（情感词数量、aspect数量是否匹配，分号是否正确）。

3.若运行中突然退出并且提示```[INFO]: WARNIGNS! The content is different at row xxx, column xxx```，请检查两个文件的xxx行的content是否一样，并再次运行。

4.Windows测试正常，若其他系统下不能正确运行请尝试改变文件编码（ANSI、GBK），或修改本脚本强制用UFTF-8打开。

5.如有其他bug请尽快反应。

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
2. 若编码错误，例：（`UnicodeDecodeError: 'gbk' codec can't decode byte 0xa2 in position 50:      illegal multibyte sequence"`）这是由于python在windows下读写文件时默认以ansi方式读写，请检查您的文件编码，尝试改为ansi编码再运行。
3. 命令行下可用 Tab 补全文件名。
