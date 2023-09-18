#object类是所有类的父类，因此所有类都具有object类的属性和方法，
#内置函数dir()可以查看指定实例对象的所有属性
#object有一个叫__str__()的方法，用于返回一个对于"对象的描述",对应于内置函数str()经常
#用于print()方法，帮我们查看对象的信息，因此我们会经常对__str__()方法进行重写
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):#重写object类的__str__()方法，返回一个对对象的描述，不重写的话，默认会输出内存地址
        # print(super().__str__())#调用父类的__str__()方法
        return '我叫{0}，今年{1}岁了'.format(self.name,self.age)
stu=Student('张三',232)
print(dir(stu))
print(stu)