print(1)
'''文件的读写原理：
文件的读写俗称I/O操作。
文件读写操作流程：python操作文件 打开或者新建文件 读写文件 关闭资源
由python解释器进行运行.py文件，在运行过程中会调用操作系统的资源。
在运行.py文件时会访问磁盘上的文件，将磁盘文件上的内容传送到python程序称为读，否则称为写。
'''
'''文件的读写操作：
用内置函数open()创建文件对象：
一个程序中的对象对应于磁盘中的真实文件，通过io流将磁盘文件中的内容与程序中对象的内容进行同步
语法规则：file=open(’filename‘,‘mode’,encoding=‘编码格式’]) 编码格式默认为gbk
解释：file为创建的文件对象
open（）为创建文件对象的函数
filename为创建或者打开的文件名字
mode为打开模式，w为写，r为读，默认为读
encoding：默认文本文件的字符编码格式为gbk
'''
file=open('zisheng.txt','r',encoding='utf-8')
print(file.readlines())
file.close()