class Student(object):
    def __init__(self,name,age):#初始化方法，将局部变量的值赋值给实例变量，实例变量是类的所有实例对象所共有的
        self.name=name
        self.age=age
    def show(self):#实例方法，该方法也是所有实例对象所共有的
        print(self.name+'在吃饭')
stu1=Student('张三',20)
stu2=Student('李四',30)
print("由于python是动态语言，因此可以动态的绑定属性和方法")
print('---------动态绑定属性------------')
stu1.sex='男'
stu2.sex='女'
print(stu1.name,stu1.age,stu1.sex)
print(stu2.name,stu2.age,stu2.sex)
print('---------动态绑定方法--------------')
def fact():
    print('因为python是动态语言，因此可以动态的绑定方法')
stu1.fact=fact
stu2.fact=fact
stu1.fact()
stu2.fact()
# stu1.show()
# stu2.show()
