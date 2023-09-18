#print("helloworld")
#print("hello,world")
#print(10,1,121,21212,2121)
#print(2.2)#输出数字
# # print('zisheng8787')
# # print("yeszisheng8787")
# # print(1+1)
# op=open('d:\\zzs.txt','a+')#以写文件的方式打开文件，如果存在这个文件，就打开，如果不存在的话，就创建一个这样的文件并且打开
# print(12,file=op)#向这个文件中输入helloworld，可以是字符串或者数字等等
# op.close()
# print("http:\\\hello","world","zisheng")
# print("hello\rwor")
# print(r"hello\bworld")
# ans='zisheng'
# print("类型",type(ans))#python中不需要定义变量，我们可以直接使用，但是我们可以采用type（）来获取数据类型，
# # 字符串类型为str，整数类型为int，浮点数类型为float
# print("内存地址",id(ans))#变量的内存地址采用id()获取
# print("值",ans)#变量的值可以直接输出
# n1=10
# n2=-19
# n3=0
# print(n1,type(n1))
# print(n2,type(n2))
# print(n3,type(n3))
# print("二进制",0b101)#二进制采用0b来头
# print("八进制",0o175)#八进制采用0o开头
# print("十进制",1991)#默认为十进制
# print("十六进制",0xAABB)#十六进制采用0x开头
#浮点数类型，即float类型
# a=3.1415926
# print(a,type(a))#浮点数类型，即小数类型
# #由于浮点数类型的不精确性，在使用浮点数进行计算的时候，可能会出现小数位数不精确的情况
#准确的情况：例如。输出1.1+2.1
# print(1.1+2.1)
#不准确的情况，例如输出1.1+2.2
# print(1.1+2.2)#直接进行输出1.1++2,2，答案为3.30000000000...3,出现这种情况的原因是浮点数在计算机当中是采用二进制进行存储的。
#解决方案：导入模块decimal即可
# from decimal import Decimal
# print(Decimal('1.1')+Decimal('2.2'))
#bool类型，用来表示真或者假的值，true表示真，false表示假，与其他语言不同，python中bool类型的值是可以转化为整数进行参与运算的，
# 其中true对应1，false对应于0
#例子：
# a1=True#注意第一个字母必须是大写的，不然会报错
# a2=False
# #输出a1和a2的值以及数据类型
# print(a1,type(a1))
# print(a2,type(a2))
# print(a1+1)#此时等价于1+1的结果，输出2，因为True等价于1
# print(a2+1)#等价于0+1的结果，输出1，因为false等价于0
#字符串类型str
#字符串又称为不可变的字符序列，可以采用单引号或者双引号或者三引号来进行定义
#注意：如果使用单引号或者双引号的时候，字符串必须写在一行上,而使用三引号的话，字符串可以分开写在多行上
# str1="zisheng8787"
# str2='qiushuang'
# str3="""zisheng
# zisheng
# dasdas"""
# print(str1,type(str1))
# print(str2,type(str2))
# print(str3,type(str3))
#数据类型转换
# name='张三'
# age=20
# print(type(name),type(age))#可以发现二者的数据类型不同，‘+’为连接运算符
# print("我叫"+name+"今年，"+str(age)+"岁")#可以进行类型转换，将整数类型转换为str类型，即字符串类型
# a=10
# b=10.2
# c=False
# print(type(a),type(b),type(c))#输出三个变量的数据类型
# print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))#输出三个变量转换为字符串类型的值以及三个变量转化为字符串类型的变量类型
# a='190.22'
# b=19.2
# c="19.12"
# d="zisheng"
# print(type(a),type(b),type(c),type(d))
# print(int(a))#将字符串类型“190“转化为整数类型190，前提是这个字符串为数字串,并且这个字符串不为小数串，才可以直接转化为整数类型
# print(int(a),type(int(a)))
# print(int(b),type(int(b)))#将float类型转化为int类型，即只包含整数部分
# print(int(d),type(int(d)))
# print(type(a),type(b),type(c),type(d))
# print(float(a),type(a))
# print(float(b),type(float(b)))
# print(float(c),type(float(c)))
# print(float(d),type(d))#如果字符串中的数据类型如果为非数字串，则不允许进行转换
#单行注释,直接采用#进行单行注释
# print("zisheng8787")
#多行注释，直接采用单三引号或者双三引号进行注释
"""
dsa
das
da
"""
#中文编码的声明注释：在文件开头加上声明注释，用以指定文件的编码格式
#即文件开头加上#conding:utf-8,即可指定文件的编码格式为utf-8字符集
#python当中的input函数,函数返回值默认是str类型，如果要想转化为int类型或者float类型的话，需要进行类型转换
#注意：input函数执行一次之后需要输入一个回车，才能继续读入下一个数
# a=input("大声想要什么礼物呢")
# print(a,type(a))#可以发现，输出的a的数据类型为str字符串类型
#不进行类型转换。默认input函数返回值为字符串类型
#例子：从键盘输入两个数，求两个数的和
# a=input("请输入一个加数：")
# b=input("请输入另外一个加数：")
# print(type(a),type(b))
# print(a+b)#可以发现输出的a和b的数据类型为字符串str类型，并且a+b的结果为两个字符串相加的结果，此时+为连接运算符
#解决方案：进行类型转换，
#输出的时候进行类型转换
#print(int(a)+int(b))#此时输出的值才是两个数相加的结果
#输入的时候直接进行类型转换
# a=int(input("请输入一个加数"))
# b=int(input("请输入另一个加数"))
# print(a+b)
#输入完成之后进行类型转换
# a=int(a)
# b=int(b)
# print(a+b)
#python当中的运算符
#python当中的基本运算符
# print(2+3)#加法运算
# print(2-3)#减法运算
#print(222222222222222222222*32222222222222222222222222222222222)#乘法运算，这一点与c语言不同，python当中的数默认是无限大的
# print(2/3)#除法运算，这与c语言不同，c语言的除法运算是整除运算
# print(3//2)#整除运算
# print(11%2)#模运算，即取余运算
# print(2**4)#幂运算，即2的四次方
#带正负号整除运算，注意此时如果一正一负的运算，遵循规则向下取整,同正同负不影响
# print(9//4)
# print(-9//-4)
# print(-9//4)
# print(9//-4)
#带正负号的模运算,遵循公式：余数=被除数-除数*商
# print(9%-4)#9-（-4）*（-3）=9-12=-3
# print(-9%4)#-9-4*(-3)=-9+12=3
#python当中的赋值运算符:运算顺序为从右到左
# a=3+4
# print(a)
#支持链式赋值,多个变量共享一个内存地址
# a=b=c=1;
# print(a,id(a))
# print(b,id(b))
# print(c,id(c))
#参数赋值
# a=100
# a+=2
# print(a)
# a-=2
# print(a)
# a*=2
# print(a)
# a/=2
# print(a)
# a//=2
# print(a)
# a%=3
# print(a)
#支持系列解包赋值
# a,b,c=1,2,3#将等于1，b等于2，c等同于3，注意：前后要进行对应
# print(a,b,c)
# a,b=1,2
# print("交换之前：",a,b)
# a,b=b,a#交换a和b的值
# print("交换之后：",a,b)
#比较运算符
# a,b=10,20
# print("a>b吗？",a>b)
# print("a<b吗？",a<b)
# print("a>=b吗?",a>=b)
# print("a<=b吗？",a<=b)
# print("a!=b吗？",a!=b)
# print("a==b吗？",a==b)
'''
在python中，一个=号赋值运算符，两个等号即==为比较运算符
u一个变量由三部分组成，即标识，类型和值
’==‘比较运算符比较的是值而不是类型，如果想要比较类型，应该采用is
'''
# a=10
# b=10
# print(a==b)#true，说明a与b的值即value值相等
# print(a is b)#true，说明a与b的标识相同，即id相同
# print(id(a),id(b))#输出a与b的id
#以下代码没学过，后面会学到
# list1=[11,22,33,44]
# list2=[11,22,33,44]
# print(list1==list2)#true说明list1和list2的值相同
# print(list1 is list2)#false,说明list1和list2的id不相同
# print(id(list1),id(list2))
# print(list1 is not list2)#true,说明list1和list2的id不相同
#布尔运算符
# a,b,=1,2
# print("-------------and 且-----------------")
# print(a==1 and b==2)#true,说明a等于1且b等于2
# print(a==1 and b<2)#false,说明a等于1且b不小于2,true and false ->false
# print(a!=1 and b==2)#false,false and true->false
# print(a!=1 and b!=2)#false,false and false->false
# print("---------------or 或者----------------")
# print(a==1 or b==1)#true,true or false->true
# print(a==1 or b==2)#true,true or true->true
# print(a!=1 or b==2)#true,false or true->true
# print(a!=1 or b!=2)#false,false or false->false
# print("----------------not 对bool类型操作数取反-------------")
# f1=True
# f2=False
# print(not f1)
# print(not f2)
# print("-------------in 与not in----------------")
# s='zisheng8787'
# print('z'in s)
# print('s'not in s)
#位运算符：将数据转化成二进制进行计算
#位与&：即对应数位同为1，结果数位才为1，否则为0
# print(4&8)#按位与&，对应数位同为1时结果数位才为1
#位或|：即对应数位都是0，结果数位才是0，否则为1
# print(4|8)#按位或，对应数位都为0时结果数位才为0，否则为1
#左移位运算符：<<,高位溢出舍弃，低位补0。左移一位相当于乘以2，左移n位相当于乘以2^n
# print(4<<1)#答案为8，即左移一位相当于乘以2，4*2=8
# #右移位运算符:>>,低位溢出舍弃，高位补0，右移一位相当于除以2，右移n位相当于除以2^n
# print(4>>2)#答案为1，右移动两位相当于除以4
#python当中的运算符的优先级
#算数运算符>位运算>比较运算>bool运算>赋值运算符
#将大象放在冰箱中
# print("---------程序开始----------")
# print("1.把冰箱门打开")
# print("2.将大象放在冰箱里")
# print("3.关闭冰箱")
# print("----------程序结束----------")
'''对象当中的布尔值
python当中的一切皆对象，所有对象都有一个布尔值
获取对象的布尔值：采用内置函数bool()函数
false 数值0 None 空字符串 空列表 空元组 空字典 空集合的布尔值都为空
'''
# print("--------------------以下对象的布尔值均为false---------------------")
# print(bool(False))
# print(bool(0))
# print(bool(0.0))
# print(bool(''))#空字符的bool值为false
# print(bool(""))#空字符串的布尔值为false
# print(bool([]))#空列表的布尔值为false，列表采用方括号表示，元组采用小括号表示
# print(bool(list()))#空列表的布尔值为false
# print(bool(()))#空元组采用小括号进行表示，空元组的布尔值为false
# print(bool(tuple()))#空元组的布尔值为false
# print(bool({}))#空字典的布尔值为false，空字典采用{}表示
# print(bool(dict()))#空字典的布尔值为false
# print(bool(set()))#空集合的布尔值为false
# print("--------------------其他对象的布尔值均为true-------------")
# print(bool(True))
# print(bool('zisheng8787'))
# money=1000
'''pyhton当中的组织结构:选择结构'''
#单分支结构：
# a=int(input("请输入取款金额:"))
# if a<=money:
#     money-=a
#     print("取款成功，余额为:",money)
# else:
#     print("余额不足，无法取款！")
#双分支结构：
# a=int(input("请输入一个整数"))
# if a%2==0:
#     print(a,"偶数")
# else:
#     print(a,"奇数")
#多分支结构:
# a=int(input())
# if a>=90 and a<=100:
#     print("成绩为A")
# elif a>=80 and a<90:
#     print("成绩为B")
# elif a>=70 and a<80:
#     print("成绩为C")
# elif a>=60 and a<70:
#     print("成绩为D")
# elif a>=0 and a<60:
#     print("成绩为E")
# else:
#     print("成绩有误，不在有限的分数范围之内")
#python当中独特的写法，和数学表达式写法一样，其他语言不可用
# a=int(input("请输入一个成绩分数"))
# if 90<=a<=100:
#     print("成绩为A")
# elif 80<=a<90:
#     print("成绩为B")
# elif 70<=a<80:
#     print("成绩为C")
# elif 60<=a<70:
#     print("成绩为D")
# elif 0<=a<60:
#     print("成绩为E")
# else:
#     print("输入的成绩有误，不在有效的分数之内")
#分支结构，嵌套if的使用
# a=int(input("请输入一个整数"))
# if a>=60:
#     if a%2==0:
#         print("分数大于等于60，并且分数为偶数")
#     else:
#         print("分数大于等于60，但是分数为奇数")
# else:
#     if a%2==0:
#         print("分数小于等于60，并且分数为偶数")
#     else:
#         print("分数小于等于60，但是分数为奇数")
#条件表达式:双分支结构的简写
#从键盘输入两个整数，比较两个数的大小
# a=int(input("请输入一个整数"))
# b=int(input("请输入另外一个整数"))
# print("----------常规写法------------")
# if a>=b:
#     print(str(a)+"大于等于"+str(b))
# else:
#     print(str(a)+"小于等于"+str(b))
# print('--------使用条件表达式-----------')
# print(str(a)+"大于等于"+str(b) if a>=b else str(a)+"小于等于"+str(b))
#pass语句：什么都不做，只是一个占位符，用在语法上需要语句的地方
# 当我们搭建好语法结构，但是没有想起来怎写代码的时候，可以使用pass语句。pass语句可以与if语句的条件执行体 for-i语句的条件执行体以及定义函数时的函数体一起使用。
# answer=input("你是会员吗？Y/N")#读入一个字符，代表是不是会员，返回值为字符串类型
# if answer=="Y":
#     pass
# else:
#     print('不是会员')
# age=int(input("请输入你的年龄:"))
# if age:#如果年龄为true的话，直接输出年龄的值
#     print(age)
# else:
#     print("年龄为",age)
'''产生随机数：
先导入random模块，调用random的randint方法进行产生即可。randint()函数的参数是产生随机数的范围，直接用，隔开即可
'''
# import random
# print(random.randint(10,100))