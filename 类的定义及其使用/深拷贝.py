class Person(object):
    def __init__(self,head,leg):
        self.head=head
        self.leg=leg
class Head(object):
    pass
class Leg(object):
    pass
head_=Head()#创建Head对象，并且用变量head_去指向它，即变量head_中存储的时Head对象的内存地址
leg_=Leg()#创建Leg对象,并且用变量leg_去指向它，即变量leg_中存储的是leg对象的内存地址
person_=Person(head_,leg_)#创建一个person对象，初始化Person对象的实例属性，实例属性分别是head实例对象和leg实例对象
#初始化完成之后用变量person_指向创建的Person对象，即person_中存储的是所创建Person对象的内存地址
import copy
person__=copy.deepcopy(person_)#深拷贝person_对象，拷贝源对象并且递归拷贝子对象，用变量person__指向拷贝的源对象，存储
print('--------------------深拷贝---------------------')
print('person_对象的内存地址及其属性的内存地址',id(person_),id(person_.head),id(person_.leg))
print('person__对象的内存地址及其属性的内存地址',id(person__),id(person__.head),id(person__.leg))

