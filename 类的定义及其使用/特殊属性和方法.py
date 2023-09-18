#特殊属性：__dict__
#特殊方法：__len__() __add__() __new__() __init__()等等都是特殊方法
#特殊属性: __dict__():获得类对象或者实例对象所绑定的所有属性和方法的字典
# class A(object):
#     pass
# class B(object):
#     pass
# class C(A,B):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class D(A):
#     pass
#
# x=C('张三',20)
# print('-------------获得实例对象的所绑定的所有属性的字典------------------')
# print(x.__dict__)#{'name': '张三', 'age': 20} 即绑定了两个属性，属性值为张三和20
# print("-------------获得类对象所绑定的所有属性和方法的字典-------------------")
# print(C.__dict__)#{'__module__': '__main__', '__init__': <function C.__init__ at 0x00000208AE0A59E0>, '__doc__': None} 既有属性又有方法
# print('-------------获得实例对象所属的类----------------')
# print(x.__class__)#<class '__main__.C'>输出实例对象所属的类
# # print(C.__class__)#<class 'type'> 如果是类对象的话，则会输出其所属类型，
# print('-------------获得一个类的所有父类------------------')
# print(C.__bases__)#(<class '__main__.A'>, <class '__main__.B'>)
# print('-------------获得一个类离他最近的一个父类-----------')
# print(C.__base__)#<class '__main__.A'>
# print("-------------获得一个类的层次结构-----------------")
# print(C.__mro__)#(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# print('------------------获得一个类的所有子类---------------------')
# print(A.__subclasses__())#[<class '__main__.C'>]
'''特殊方法：
1. __len__()方法：通过重写__len__()方法让内置函数len()的参数可以是自定义类型
2. __add__()方法：通过重写__add__()方法，可以自定义对象具有+功能
3. __new__()方法：用于创建对象
4. __init__()方法：对创建的对象进行初始化
'''
'''__add__()方法：通过重写__add__()方法: 可以自定义对象具有+功能'''
# a=10
# b=20
# c=a+b
# print('------输出两个整数对象的相加的结果')
# print(c)
class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self,other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
stu1=Student('zisheng8787')
stu2=Student("李四")
# print('------------输出两个实例对象相加的结果-------------')
# stu=stu1+stu2
# stu_=stu1.__add__(stu2)
# print(stu,stu_)#张三李四 张三李四
'''__len__()方法：通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
'''
a=[11,22,33,44,55,66]
print('--------输出列表对象的长度----------')
print(len(a))
print(a.__len__())#此方法对应与内置函数len(),也可以获得列表对象的长度
print('---------输出实例对象的长度----------')
print(len(stu1))
print(stu1.__len__())#此方法对应于内置函数len(),用于输出实例对象的长度
