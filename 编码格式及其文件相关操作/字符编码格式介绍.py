print(1)
'''
.py文件默认的编码格式为UTF-8，可以在文件开头设置编码格式   在文件开头加上这一句话 #encoding=gbk
.py文件在磁盘上使用UTF-8进行存储（外存）
python的解释器采用的是unicode（内存）
unicode:定长编码，一个字符采用两个字节进行表示
UTF-8:变长编码：一个字符采用1~4个字节进行表示，英文一个字节，汉字三个字节
GBK：英文1个字节，汉字2个字节
'''

