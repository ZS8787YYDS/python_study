print(1)
'''r：以只读的方式打开文件'''
# file=open('zs.txt','r',encoding='utf-8')
# a=file.readline()#读取文本文件中的一行内容
# a=file.read()#读取所有内容
# print(file.read(2))#从文件中读取两个字符进行输出
# print(type(a))#字符串类型<class 'str'>
# print(a)
# lst=file.readlines()#读取文件中的每一行数据，包括换行符，将它作为一个字符串对象存入到列表当中
# print(lst)
# file.close()
'''w：以只写的方式打开文件，如果文件不存在就创建，如果文件存在的话，就覆盖掉原来的内容，重写进行写入，文件指针指向开头处'''
# file=open('8787.txt','w',encoding='utf-8')
# file.write('侯自胜加油加油呀！！！')#将一行字符串中的内容写入文件当中
# a=['侯自胜\n','你还不赶紧学习\n','干啥呢']
# file.writelines(a)#将一个字符列表当中的元素写入文件当中。
'''a：以追加的方式打开文件，如果文件不存在就创建一个，文件指针指向开头位置，如果文件存在的话，就在文件的末尾追加内容，文件指针指向文件末尾，'''
# file=open('zs.txt','a',encoding='utf-8')
# # file.write('你是傻逼')#在文件的尾部加入一个字符串内容
# # file.close()
# a=['侯自胜\n','你还不赶紧学习\n','干啥呢']
# file.writelines(a)
# file.close()
'''a+：以读写的方式打开文件，既能读又能写'''
file=open('zs.txt','a+',encoding='utf-8')
file.write('一会不知道吃啥饭呢！！！')#将字符串中的内容写入到文件中
file.close()
# file=open('zs.txt','a',encoding='utf-8')
'''tell()返回文件指针当前的位置'''
# print(file.tell())#输出文件指针当前的位置
'''flush（）:用于将缓冲区的内容写入文件，但是不关闭文件'''
'''close():用于将关闭文件，同时释放系统资源'''
# print(file.readline())
# file.close()
# file.write('hello')
# file.flush()
# file.write('world')
# file.close()




