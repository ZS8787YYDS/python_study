# #字典
# 什么是字典
# 字典是python当中的数据结构之一，与列表一样是一个可变序列，可变序列说明字典可以像列表一样进行增加 删除 修改操作
# 字典的元素是以键值对的方式进行存储数据，每一个key值对应一个value，字典是一个无顺序的序列.无序序列说明字典当中的元素存放是没有顺序的
#当我们向字典中进行存放元素时，首先要算这个元素在字典的位置，即通过哈希函数来计算，字典中的key必须是不可变序列,相当于c语言或者c++语言的哈希表。查询操作非常快.
# 字典是采用花括号进行定义的，这一点与列表不同,列表是采用方括号进行定义的。
#字典的创建方式:
#直接采用花括号进行创建
scores={'zisheng8787': 11,'qiushuang': 11,'yuanruhui': 122}
# print(scores)
# print(scores,type(scores))
#采用内置函数dict()进行创建
# scores=dict(name='zisheng',age=20)
# print(scores)
# #创建空字典：直接采用花括号进行创建，括号内为空值
# student={}#创建一个空字典
# print(student)
#字典的常用操作：
#字典当中元素的获取：
#采用方括号的方式进行获取:如果字典当中不存在指定的key的话，或抛出一个keyError
# print(scores['qiushuang'])#获取键为'qiushuang'的值
# #采用get（）方法进行获取:如果字典当中不存在指定的key。不会抛出keyerror，而是返回none，
# #但是可以通过参数设置默认的value，以便于键不存在时返回
# print(scores.get("zisheng8787"))#获取键为‘zisheng8787’的值
# print(scores.get('zisheng',8787))#键为zisheng的值在字典中不存在，则会输出一个默认值8787
'''字典的增加 删除 修改操作'''
#key的判断：in和not in
#in: 指定的key在字典中不存在时返回false，存在时返回true
#not in: 指定的key在字典中不存在时返回true，存在时返回false
# print('zhangsan' in scores)
# print('zhangsan' not in scores)
'''字典元素的删除'''
# del scores['zisheng8787']#删除键为'zisheng'的键值对
# scores.clear()#删除字典当中的所有元素，即请空字典
'''字典元素的新增'''
# scores['zhangsan']=90#新增一个键为'zhangsan',值为90的键值对，存入到字典中
# print(scores)
'''字典元素的修改操作'''
# scores['zisheng8787']=8787#修改键为'zisheng8787'的值为8787
# print(scores)
'''获取字典视图的三个方法'''
#keys()：获取字典当中的所有key
#values():获取字典当中的所有的value
#items()：获取字典当中所有键值对
# keys=scores.keys()#获取字典当中的所有key，存到keys变量当中
# print(keys)#获取字典当中的所有key,并且输出keys的类型
# values=scores.values()#获取字典当中的所有value值
# print(scores.values(),type(values))#输出字典当中的所有value，并且输出values的类型
# items=scores.items()#获取字典当中的所有键值对
# print(scores.items(),type(items))#输出字典当中的所有键值对，并且输出items的类型
# print(list(items))
'''字典元素的遍历
语法格式：for i in scores
            print(i)
        每次获取到的i时字典当中的key
'''
'''注意：由于是对字典内元素的遍历，因此每个元素在字典当中都是存在的，因此既可以使用方括号方式进行获取key对应的值
    也可以采用get（）方法进行获取字典当中key对应的值
'''
#方式一：采用get方法进行遍历
# for i in scores:
#     print(i,scores.get(i))
#方式二：采用方括号的方式进行遍历
# for i in scores:
#     print(i,scores[i])
'''字典的特点：
1.字典当中的所有元素都是一个键值对，即每一个key对应一个value值,key不允许重复，但是value可以重复
2.字典当中的元素都是无顺序的，先存入字典的元素不一定在前，后存入的元素也不一定在后，实际上是根据每个
元素的值计算它的哈希函数值来确定位置的，查询效率非常快
3.字典当中的key必须是不可变对象
4.字典也可以根据需要动态地伸缩。不需要事先进行分配空间，会随着内部元素的增加而增加，元素的减少而减少
5.字典会浪费掉较大的内存，是一种用空间换时间的数据结构
'''
'''字典生成式：生成字典的公式
内置函数：zip()：用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
语法格式：例如：{item.upper(): price for item,price in zip(items,prices)}
'''
'''defaultdict类：
defaultdict是Python标准库collections模块中的一个类。defaultdict类是dict类的一个子类，它具有与dict类相同的功能，
但是在处理缺失键（即字典中不存在的键）时有一些不同之处。
defaultdict的初始化需要传递一个参数，用于指定默认值的类型。在这里，int作为参数传递给defaultdict，意味着默认值为整数类型（0）。
也就是说，如果对于一个不存在的键进行访问时，会返回默认值0，而不会引发KeyError异常
例子：
from collections import defaultdict
a = defaultdict(int)
print(a['key1'])  # 输出：0，因为'key1'不存在于字典a中，使用了默认值0
print(a['key2'])  # 输出：0，因为'key2'不存在于字典a中，使用了默认值0
在上述代码中，我们创建了一个名为a的defaultdict对象，并使用整数类型作为默认值。
然后，我们通过访问字典中不存在的键'key1'和'key2'，会返回默认值0，而不会引发KeyError异常。
defaultdict类的优点在于当访问一个不存在的键时，可以自动创建该键，并赋予指定的默认值类型，
而不需要手动处理键不存在的情况。
'''
# list1=['zi','sheng','qiu','shuang']
# list2=[10,20,30,40]
# dd={i : j for i,j in zip(list1,list2)}
# #i是自定义的表示字典中key的变量，j是自定义的表示字典中value的变量，i.upper()表示计算字典中key的表达式。
# #执行过程是依次从列表List1和list2中取出一个元素值赋值给i和j，然后通过字典中key和value的表达式计算出key和value，
# # 组成一个元组，最后返回由这些元组组成的列表
# print(dd,type(dd))#输出字典中的所有元素值以及变量dd的类型
'''总结：
字典的创建：
1.使用{}花括号
2.内置函数dict()
3.使用字典生成式
对字典的常用操作：
1.获取value值：
（1）字典名字[key] 注意：如果key不存在，则会抛出错误
（2）字典名字.get(key) 注意：此方法不会抛出错误，但是如果key不存在，会抛出一个None。我们可以设置默认值，当key不存在时抛出即可.语法格式为：字典名字.get(key,默认值)
2.删除键值对:del 字典的名字[key]
3.修改键对应值/增加键值对
字典的名字[key]=value
5.in/not in
6.清空键值对：字典名字.clear() 注意：会清空字典内的所有元素
in:若key在字典当中存在，则返回True，否则返回False
not in:若key在字典中不存在，返回True,否则返回False
'''