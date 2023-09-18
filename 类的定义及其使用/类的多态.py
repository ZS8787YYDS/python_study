#动态就是具有多种形态，指的是即便不知道一个变量所引用的对象到底是什么类型，
#仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法。
class animal(object):
    def show(self):
        print('动物要吃东西的')
class dog(animal):
    def show(self):
        print('狗吃骨头')
class cat(animal):
    def show(self):
        print('猫吃鱼')
class person(animal):
    def show(self):
        print("人吃五谷杂粮")
def fact(a):
    a.show()
fact(dog())
fact(cat())
fact(person())
fact(animal())
'''总结：
多态就是具有多种形态，即即便不知道变量所引用的对象是什么类型，仍然可以通过这个变量调用方法，在运行过程中，
根据变量所引用对象的类型，动态地决定调用哪个对象中的方法。
'''
