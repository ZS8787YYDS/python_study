#变量的赋值操作：只是形成两个变量，两个变量指向同一个对象
class Cpu(object):
    pass
class Disk(object):
    pass
class Computer(object):
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
cpu1=Cpu()##创建一个Cpu类实例对象，并且让变量cpu1指向它
cpu2=cpu1#将变量s1的值赋值给变量s2
print('s1的内存地址为:{0}'.format(id(cpu1)))
print('s2的内存地址为:{0}'.format(id(cpu2)))
'''可以发现s1和s2是两个不同的变量，但是他们指向同一个对象'''
#类的浅拷贝：使用copy模块的copy函数
'''
python的拷贝一般都是浅拷贝，拷贝时，只拷贝原对象，原对象所包含的子对象内容不拷贝，拷贝之后源对象和拷贝对象占有不同的内存地址
但是源对象和拷贝对象所有子对象的内存地址相同。
'''
#类的深拷贝：使用copy模块的deepcopy函数，
'''
递归拷贝对象中的包含的子对象，源对象和和拷贝对象所有的子对象也不相同。
'''
disk1=Disk()#创建一个Disk类实例对象，并将disk1指向它
computer1=Computer(cpu1,disk1)#创建一个Computer类实例对象，初始化完成之后，使变量computer1指向它
import copy#导入copy模块
# print('--------浅拷贝-------------：')
# computer2=copy.copy(computer1)#将拷贝computer1的值赋值给computer2
print('----------深拷贝------------')
computer2=copy.deepcopy(computer1)
print('computer1的内存地址及其相应的实例属性值',id(computer1),computer1.disk,computer1.cpu)
print('computer2的内存地址及其相应的实例属性值',id(computer2),computer2.disk,computer2.cpu)
'''可以发现computer1和computer2占有两个不同的内存地址，是不同的变量，但是子对象的内容是相同的，
即拷贝时只拷贝原对象，原对象所包含的子对象不拷贝。'''

