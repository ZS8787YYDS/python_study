#包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下
#包的作用：
#1. 代码规范
#2. 避免模块名称冲突
#包与目录的区别：
#1. 包含__init__.py文件的目录称为包
#2. 目录里通常不包含__init__.py文件
#包的导入：import 包名.模块名
#使用import进行导入，只能导入包名，或者模块名
# import page
# import page.calc as p
# print(p.a,p.b,p.c)
#使用from import进行导入，既可以导入包名，又可以导入模块名
# from page import calc as p
# print(p.a,p.b,p.c)
print(1)
'''python当中程序的组成：
一个程序由很多个包组成，每个包有很多模块组成，不同的包之间的模块可以相同，他们具有不同的功能，一个模块有很多函数 很多变量 很多类 很多语句组成
，一个类当中可由很多类属性，类方法，实例方法，静态方法组成。
'''

