# dataHelper

An useful data helper

----

> updatetime 2019/02/28/ 01:08

#### removeinvalidlines.py

用来移除文件中的无效行，执行时会提示输入两个字符串，第一个要求输入待处理文件名称（或相对/绝对路径），第二个要求输入输出文件名称（或相对/绝对路径），运行结束后，会生成一个处理后的文件，并且会在控制台输出当前总的有效行数。

#### conflicthandling.py

用来比较两个不同文件的差异，执行时要求输入两个字符串，分别为两个待处理文件名（或相对/绝对路径）。处理完成后，会在控制台输出两个文件冲突发生的位置，同时也会在文件目录下生成一个ConflictInfo.csv文件来记录两个文件冲突之处。同时请注意，在使用该文件时，请确定两个待处理文件的前两列完全一致（即id和content），排序也要完全一样！

另外：

1. 请使用`python3`运行本文件。
2. 若编码错误，例：（`UnicodeDecodeError: 'gbk' codec can't decode byte 0xa2 in position 50:      illegal multibyte sequence"`）这是由于python读写文件时默认以ansi方式读写，请检查您的文件编码，尝试改为ansi编码再运行。
