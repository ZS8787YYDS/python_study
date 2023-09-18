# 封装：提高程序的安全性。
# 将属性和方法封装在类对象中，在方法内部对属性进行操作，在类对象的外部调用方法，这样便可无需关心方法内部的实现细节，从而隔离了复杂度。
# 在python当中没有专门的修饰符用于属性的私有，如果不希望该属性在类对象外部被访问，则在初始化方法中将实例属性前面加两个_
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.__age=age #将局部变量的值赋值给实例变量的时加上__,表明次在类对象外部不能被访问
    def fact(self):
        print('我叫{0},今年{1}岁了'.format(self.name,self.__age))
stu1=Student('张三',20)#创建Student类实例对象stu1
print(stu1.name)#输出stu1对象的name属性值
# print(stu1.age)不能输出stu1对象的age属性值，因为age属性值在类对象外部是不能被访问的
stu1.fact()#调用类的fact()方法，
# print(stu1._Student__age) 可以访问到在类对象外部不能被访问的属性，但
# print(dir(stu1)) 可以获取到实例对象所有可以使用的属性及其方法