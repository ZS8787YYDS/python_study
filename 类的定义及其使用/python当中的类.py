'''python当中的类是由以下几部分组成：
1. 类属性：在类中方法之外定义的变量就是类属性，被该类的所有对象所共享
2. 实例方法：在类中定义的函数称为方法，实例方法中含有参数self
3. 静态方法：在类中定义的函数，并且有@staticmethod进行修饰，无参数，是可以使用类名直接访问的方法
4. 类方法： 在类中定义的函数，并且有@classmethod进行修饰，含有参数cls，是可以由类名直接访问的方法
'''
# 类名称由一个或者几个单词组成，每个单词的首字母大写
# 在类中定义的称为方法，在类外定义的称为函数
# 创建一个Student类
class Student:
    # 定义在类中的变量是类属性
    native_place='zs8787'
    # 初始化:self.name称为实体属性，name称为局部变量
    def __init__(self,name,age):
        self.name=name
        '''将局部变量name的值赋值给实体属性self.name'''
        self.age=age

    # 实例方法：
    def eat(self):
        print("学生在吃饭")
    # 静态方法：
    @staticmethod
    def method():
        print("因为我采用staticmethod进行修饰，因此我是静态方法")
    # 类方法：
    @classmethod
    def drink(cls):
        print("因为我采用了classmethod进行修饰，因此我是类方法")
#对象的创建又称作类的实例化,有了实例，就可以调用类中的内容
# 创建对象的语法：实例名=类名()
# 创建一个Student类对象
stu=Student("自生",21)
# print('-----------实例对象的地址 类型及其值---------------')
# print(id(stu))
# print(type(stu))
# print(stu)
# print('------------类对象地址 类型和值---------------------')
# print(id(Student))
# print(type(Student))
# print(Student)
# print(stu.age)
# print(stu.name)
print("------------实例方法的使用方式---------------")
stu.eat()#调用方式为对象名.方法名(),不需要传递参数
Student.eat(stu)#此调用方式是类名.方法名(参数是类对象),等价于对象名.方法名().
print("------------类方法的使用方式------------")
Student.drink()
print("-------------静态方法的使用方式----------")
Student.method()
print("-------------类属性的使用方式------------")
print(Student.native_place)

