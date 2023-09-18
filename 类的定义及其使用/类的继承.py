#类的继承：语法格式为class 子类名(父类1，父类2......)
#如果一个类没有继承任何类，则默认其继承object类，python支持多继承，即一个子类可以继承多个父类
#定义子类时，必须在其构造函数中调用父类的构造函数，即在其初始化方法中调用父类的初始化方法，子类具有父类
#所有的属性及其方法
#方法重写：如果子类对继承父类的某个属性或者方法不满意，可以在子类中对其方法进行重写，
# 而且可以通过super().被重写的方法名()来调用父类中被重写的方法
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print('我叫{0}，今年{1}岁了'.format(self.name,self.age),end=',')
class Student(Person):
    def __init__(self,name,age,sex):
        super().__init__(name,age)#调用父类的初始化方法
        self.sex=sex
    def show(self):
        super().show()
        print('我的性别是'+self.sex)
        # print('我叫{0}，今年{1}岁了,我的性别是{2}'.format(self.name, self.age,self.sex))
stu=Student('张三',20,'男')
stu.show()

