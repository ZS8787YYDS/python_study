import time

print(1)
'''python当中常用的内置模块
1. sys模块：与python解释器及其环境相关的标准库
2. time模块：提供与时间相关的各种函数的标准库
3. os模块：提供了访问操作系统服务功能的标准库
4. calender模块：提供了与日期相关的各种函数的标准库
5. urllib模块：用于读取来自网上(服务器)的数据标准库
6. json模块：用于使用JSON序列化和反序列化对象
7. re模块：用于字符串中执行正则表达式匹配和替换
8. math模块：用于提供算数运算函数的标准库
9. decimal模块：用于进行精确控制运算精度 有效位和四舍五入操作的十进制运算
10. logging模块：提供了灵活的记录事件、错误、警告和调试信息等日志信息的功能
'''
'''sys模块'''
# import sys
'''sys模块中的getsizeof函数用于获得对象所占的内存大小'''
# print(sys.getsizeof(21))
# print(sys.getsizeof(45))
# print(sys.getsizeof(True))
# print(sys.getsizeof(False))
'''time模块'''
'''
time模块当中的time（）函数用于获取当前系统的时间，返回的是秒数
time模块当中localtime()函数用于将当前系统的时间转化为当地时间
'''
# print(time.time())
# print(time.localtime(time.time()))
'''urllib模块：
urllib包中的request模块中的Urlopen方法可以打开某一服务器网址并且获取服务器上的数据
'''
# import urllib.request
# dataofbaidu=urllib.request.urlopen('https://baidu.com').read()
# print(dataofbaidu)


