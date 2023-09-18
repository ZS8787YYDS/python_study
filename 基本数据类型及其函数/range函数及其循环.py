#到此为止，已经学习了两种内置函数，input函数,print函数,下面来学习一下range函数
#内置函数range函数的应用：用于生成一个整数序列，返回值是一个迭代器对象
#range类型的优点：
#不管range对象表示的整数序列有多长，所有range对象占用的内存空间是相同的，因为仅仅需要存储start stop和step，
#只有当用到range对象的时候，才会去计算序列当中的相关元素，采用in与not in来判断整数序列当中存在还是不存在指定的整数
#创建range对象的三种方式：
#range(stop),只有一个参数，创建一个0到stop-1之间的整数序列，步长为1
# a=range(10)#生成一个0到9之间的整数序列，默认从0开始，步长为1
# print(a,type(a))#range(0, 10) <class 'range'>
# print(list(a))#用于查看range当中的整数序列，list是列表的意思
#range(start,stop)，含有两个参数，创建一个start到sto-1p之间的整数序列，步长为1
# a=range(1,10)#生成一个1到9之间的整数序列，默认步长为1
# print(list(a))#查看序列当中的元素
#range(start,stop,step)，含有三个参数，创建一个start到stop-1之间的整数序列，步长为step
# a=range(1,10,2)#生成一个从1到9步长为2的整数序列，
# print(a,type(a))#
# print(list(a))#输出序列当中的元素值，[1, 3, 5, 7, 9]
# '''判断指定的整数是否在序列当中，采用in或者not in'''
# print(10 in a)#false,不在学列当中
# print(1 in a)#true,1在序列当中
# print(3 in a)#true,3在序列当中
# print(10 not in a)#true,10不在整数序列当中
# print(9 not in a)#false,9在整数序列当中
#循环结构，while循环和for-in循环
#while循环:判断n+1次，执行n+1次，与if不同,if语句是判断一次，执行一次循环体
#求1到100所有偶数的和：
# a=1
# ans=0
# while a<=100:
#     if not(a%2):
#         ans+=a
#     a+=1
# print("0到4之间的和为",ans)
#for-in循环：
#in表示从表达式（字符串 序列等等）中依次取值，也称为遍历，for-in遍历的对象称为可迭代对象、
#for-in的语法结构：for 自定义的变量 in 可迭代对象:循环体。如果循环体内不需要访问自定义变量，可以将自定义变量替代为下划线
# for i in "zisheng8787":
#     print(i)
#依次输出1到100的所有整数
# for i in range(1,101):
#     print(i)
#不需要采用自定义的变量，则可以将其用下划线进行代替
# for _ in range(4):
#     print("加油 侯自胜")
'''使用一个for循环来计算1-100之间的偶数和'''
# ans=0
# for i in range(1,101):
#     if not(i%2):
#         ans+=i
# print("1到100之间偶数之和为：",ans)
#求100到999之间的所有的水仙花数：
#采用while循环：
# i=100
# while i<=999:
#     a=i%10
#     b=(i//10)%10
#     c=(i//100)%10#python当中的/为数学上的除法，//才为整除
#     if a**3+b**3+c**3==i:
#          print(i)
#     i+=1
#采用for循环进行求解：
# for i in range(100,1000):
#     a=i%10
#     b=(i//10)%10
#     c=(i//100)%10
#     if a**3+b**3+c**3==i:
#         print(i)
#使用for-in循环：
# for i in range(3):
#     a=input("请输入一个名字")
#     if a=="zisheng":
#         print("名字正确")
#         break
#     else:
#         print("名字错误，请重新输入")
#     if i==2:
#         print("输入次数过多，请稍后重新输入")
#使用while循环：
# i=1
# while i<=3:
#     a=input("请输入一个名字")
#     if a=="zisheng":
#         print("输入正确")
#         break
#     else:
#         print("输入错误，请重新输入")
#     if i==3:
#         print("输入次数过多，稍后请重新输入")
#     i+=1
#输出1到50之间所有是5的倍数：
#采用for-in循环进行解决：
# for i in range(1,51):
#     if not(i%5):
#         print(i)
#     else:
#         continue
#采用while循环解决：
# i=1
# while i<=50:
#     if i%5==0:
#         print(i)
#     i+=1
#for else语句：
# for i in range(3):
#     a=input("请输入一个名字")
#     if a=='zishneg8787':
#         print("输入正确")
#         break
#     else:
#         print("输入错误")
# else:
#     print("输入次数过多，请稍后重新输入")
#while-else语句：
# i=0
# while i<3:
#     a=input("请输入一个密码")
#     if a=='zisheng':
#         print("密码正确")
#         break
#     else:
#         if i<2:
#             print("密码输入错误，请重新输入")
#     i+=1
# else:
#     print("三次密码均输入错误，轻稍后重新输入")
#嵌套循环：
#注意：在使用print语句时，如果不想输出一个回车，可以添加一个参数，对end进行重新赋值，默认为'\n'
# print("zisheng8787")#直接输出，结尾会输出一个回车
# print("zisheng",end='')#输出之后结尾不输出回车，下一条语句将在同一行进行输出
# print("8787")
# for i in range(3):
#     for j in range(4):
#         print("*",end='')#不换行输出
#     print()#每行输出完毕之后输出一个回车
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(i)+"*"+str(j)+"="+str(i*j),end='\t')
#         # print(i,"*",j,"=",i*j,end='\t')
#     print()
#二重循环的break和continu语句：
# for i in range(4):
#     for j in range(1,11):
#         if j%2==0:
#             continue
#         print(j,end=' ')
#     print()