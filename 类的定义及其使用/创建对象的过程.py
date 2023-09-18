#特殊方法：__new__()用于创建对象：
#特殊方法:__init__()用于对创建的对象进行初始化
class Student(object):
    def __new__(cls, *args, **kwargs):#
        print('__new__被调用了，cls的内存地址为：{0}'.format(id(cls)))
        new_object=super().__new__(cls)
        print('新创建对象的内存地址为:{0}'.format(id(new_object)))
        return new_object
    def __init__(self,name,age):
        print('__init__被调用了，self的内存地址为：{0}'.format(id(self)))
        self.name=name
        self.age=age
print('object这个类对象所占的内存地址：{0}'.format(id(object)))
print('Student这个类对象所占的内存地址：{0}'.format(id(Student)))
stu1=Student('张三',20)
print('stu1这个实例对象所占的内存地址：{0}'.format(id(stu1)))
'''运行结果为：
object这个类对象所占的内存地址：140736270863856
Student这个类对象所占的内存地址：2730706380192
__new__被调用了，cls的内存地址为：2730706380192
新创建对象的内存地址为:2730706866576
__init__被调用了，self的内存地址为：2730706866576
stu1这个实例对象所占的内存地址：2730706866576
总结：可以发现通过__new__创建的对象与初始化时的self以及stu1具有相同的内存地址，Student类对象和cls具有相同的内存地址，他们代表同一对象。
执行过程：
首先将Student传给cls，然后调用object类的__new__()方法去创建一个Student对象，并且返回新创建的对象赋值给self，完成初始化操作后将
self赋值给stu1
'''



