print(1)
'''os模块是python内置的与操作系统功能和文件系统相关的模块，该模块中的语句的执行结果通常
与操作系统有关，在不同的操作系统上运行，得到的结果也不一样。
os模块与os.path模块用于对目录或者文件进行操作
'''
'''调用系统的文件'''
import os
# os.system('calc.exe')#打开计算器，相当于windows+R之后输入calc
# os.system('notepad.exe')#打开记事本
'''直接调用可执行文件'''
# os.startfile('C:\\Program Files (x86)\\Tencent\\QQ\\Bin\\qq.exe')#打开可执行文件qq.exe
# os.startfile('C:\\Program Files (x86)\\Tencent\\QQMusic\\QQMusic.exe')#打开可执行文件qq音乐
'''os模块操作目录相关函数:
getcwd()函数：获取当前的工作目录
listdir(path):返回指定路径下的文件和目录信息
mkdir(path,[,mode]):创建目录
makedirs(path1/path2/path3...[,mode])：创建多级目录
rmdir(path)：删除目录
removedirs(path1/path2.....):删除多级目录
chdir(path):将path设置为当前工作目录
'''
'''getcwd()获取当前的工作目录'''
# print("---------------当前的工作目录为：-------------")
# print(os.getcwd())
'''listdir():获取指定路径下的文件和目录信息，返回值是一个列表'''
# print('-------------获取指定路径下的目录和文件信息-------------')
# lst=os.listdir('C:\\Users\\lenovo\\Desktop\\python项目1\\编码格式及其文件相关操作')
# print(lst)
'''mkdir()函数创建目录：'''
# os.mkdir('C:\\Users\\lenovo\\Desktop\\python项目1\\编码格式及其文件相关操作\\newdirectory2')#在指定路径下创建目录
'''makedirs()创建多级目录'''
# os.makedirs('C:\\Users\\lenovo\\Desktop\\python项目1\\编码格式及其文件相关操作\\A\\B\\C')#创建多级目录
'''rmdir()删除目录'''
# os.rmdir('newdirectory2')
# '''removedirs()删除多级目录'''
# os.removedirs('A\\B\\C')
'''chdir（）改变当前的工作目录：'''
# os.chdir('C:\\Users\\lenovo\\Desktop\\python项目1\\编码格式及其文件相关操作')
# print(os.getcwd())
