#创建模块：新建一个.py文件，名称尽量不要与python自带的标准模块相同
#导入模块：格式为:from 模块名称 import 函数/类/变量 此方式导入一个模块当中指定内容
#       :或者为import 模块名称   此方式导入模块当中所有内容
#采用import 模块名称 方式导入模块
# import math
# # print(id(math))
# # print(type(math))
# # print(math)
# # print(dir(math))
# # print(math.factorial(4))
# # print(math.sqrt(3))
# # print(math.pi,math.e)
# # print(math.ceil(9.000222))#向下取整
# # print(math.floor(9.2222))#向上去整
#采用from 模块名称 import 函数/类/名称
# from math import pi
# from math import sqrt
# print(pi,sqrt(4))
#导入自定义的模块
import calc
print(calc.add(1,2))
print(calc.mul(2,3))
print(calc.div(2,3))
from calc import add
print(add(1,2))


