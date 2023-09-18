import os.path
fname='student.txt'
def menu():
    print('=========================学生信息管理系统=============================')
    print('----------------------------功能菜单------------------------------')
    print('\t1.录入学生信息')
    print('\t2.修改学生信息')
    print('\t3.删除学生信息')
    print('\t4.查询学生信息')
    print('\t5.排序')
    print('\t6.统计学生总人数')
    print('\t7.显示所有学生信息')
    print('\t0.退出')
    print('--------------------------------------------------------------------')
def main():
    while True:
        menu()
        choice=int(input('请选择一个序号\n'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice==0:
                answer=input('你确定要退出系统嘛！！！！输入y或者n\n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用，再见！！！！！')
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                modify()
            elif choice==3:
                delete()
            elif choice==4:
                search()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            else:
                show()
        else:
            print('输入的序号不对，请重新输入！！！！')
            continue
def insert():
    student_list=[]
    show()
    while True:
        id=input('请输入学生的ID，例如1000\n')
        if not id:
            print('输入的id为空，请重新进行输入')
            continue
        name=input('请输入学生的姓名\n')
        if not name:
            print('输入的姓名为空值，请重新进行输入')
            continue
        try:
            chinese_grade=int(input('请输入语文的成绩\n'))
            math_grade=int(input('请输入数学的成绩\n'))
            english_grade=int(input('请输入英语的成绩\n'))
            python_grade=int(input('请输入python的成绩\n'))
        except:
            print('输入的成绩不是整数，输入无效，请重新输入\n')
            continue
        student_message={'id':id,'name':name,'chinese':chinese_grade,'math':math_grade,'english':english_grade,'python':python_grade}
        student_list.append(student_message)
        answer=input('是否继续录入成绩,输入y或者n\n')
        if answer=='Y' or answer=='y':
            continue
        else:
            break
    access(student_list)#将学生信息录入到文件当中
    show()
    print('录入信息完成！！！！')
def access(list):
    try:
        filename=open(fname,'a',encoding='utf-8')#以追加的方式打开文件，如果文件不存在就创建一个，存在的话就在文件末尾追加内容
    except:
        filename=open(fname,'w',encoding='utf-8')
    for student in list:#遍历列表当中的所有学生的信息，将其转化为字符串写入到文件中，并且末尾加一个回车
        filename.write(str(student)+'\n')
    filename.close()
    print('信息已经保存到文件中！！！')
def modify():
    while True:
        print('==============修改之前的学生信息===============')
        show()
        student_id=input('请输入要修改的学生id\n')
        if not student_id:
            print('输入的id为空，请重新输入')
            continue
        else:
            if os.path.exists(fname):
                with open(fname,'r',encoding='utf-8') as file:
                    lst=file.readlines()
            else:
                lst=[]
            if not lst:
                print('不存在任何学生的信息，不能进行修改，请确保已经录入学生信息')
                return
            else:
                flag=False
                with open(fname,'w',encoding='utf-8') as file:#以只写的方式打开文件，会覆盖文件之前的内容
                    for item in lst:
                        dic=dict(eval(item))#将每个字符串形式的字典转化为字典形式
                        if dic['id']==student_id:
                            print('已经找到id为{0}的学生了，可以进行修改操作了'.format(student_id))
                            while True:#由于在修改学生信息的时候，可能会输错，因此采用一个死循环和try except else语句来进行修改
                                try:
                                    dic['name'] = input('请输入修改后的学生姓名\n')
                                    dic['chinese']=int(input('请输入修改后的语文成绩\n'))
                                    dic['math']=int(input('请输入修改后的数学成绩\n'))
                                    dic['english']=int(input('请输入修改后的英语成绩\n'))
                                    dic['python']=int(input('请输入修改后的python成绩'))
                                except:
                                    print('输入的成绩有误，请重新进行修改！')
                                    continue
                                else:
                                    break
                            file.write(str(dic)+'\n')
                            flag=True
                        else:
                            file.write(str(dic)+'\n')
                    if flag:
                        print('id为{0}的学生信息已经修改完毕！！！')
                    else:
                        print('修改失败，没有找到id为{0}学生的信息，请确保该学生存在'.format(student_id))
        print('============修改后的学生信息============')
        show()
        answer = input('是否话继续录入学生信息y/n\n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    print('信息修改完毕！')
def delete():
    while True:
        print('========删除之前的学生信息==========')
        show()
        student_id=input('请输入要删除的学生id:\n')
        if student_id:
            if os.path.exists(fname):
                with open(fname,'r',encoding='utf-8') as file:
                    lst=file.readlines()
            else:
                lst=[]
            flag=False
            if lst:
                with open(fname,'w',encoding='utf-8') as wfile:
                    for item in lst:
                        dic=dict(eval(item))
                        if dic['id']!=student_id:
                            wfile.write(str(dic)+'\n')
                        else:
                            flag=True
                    if flag:
                        print('id为{0}的学生信息已经被删除'.format(student_id))
                    else:
                        print('没有找到id为{0}的学生的信息'.format(student_id))
            else:
                print('不存在学生的信息，无法进行删除操作！')
                return
            print('删除之后的学生信息')
            show()#显示所有的学生信息
            answer=input('是否还继续删除学生的信息y/n\n')
            if answer=='y' or answer=='Y':
                continue
            else:
                break
        else:
            print('输入的学生id为空，请重新输入')
            continue
    print('删除完毕！！！')
def search():
    select=0
    while True:
        try:
            select=int(input('按照id查询请按1，按照姓名查询请按2\n'))
        except:
            print('输入格式不正确，请输入1或者2')
            continue
        else:
            break
    if select==1:
      id_search()
    elif select==2:
     name_search()
    print('查询完毕！！！')
def name_search():
    if os.path.exists(fname):
        with open(fname,'r',encoding='utf-8')  as file:
            lst=file.readlines()
            student_name = input('请输入查询的学生姓名\n')
            flag = False
            for item in lst:
                dic = dict(eval(item))
                if dic['name'] == student_name:
                    flag = True
                    print('id:', dic['id'], 'name:', dic['name'], 'chinese:', dic['chinese'], 'math:', dic['math'],
                          'english:', dic['english'], 'python:', dic['python'])
                    break
                else:
                    continue
            if flag:
                print('姓名为{0}的学生信息已经输出'.format(student_name))
            else:
                print('没有找到姓名为{0}的学生'.format(student_name))
            answer = input('是否继续查询学生的信息y/n\n')
            if answer == 'y':
                name_search()
            else:
                answer=input('确定不查询了吗？y/n\n')
                if answer=='y':
                    return
                else:
                    name_search()
    else:
        print('不存在任何学生信息，请先录入学生信息')
        return
def id_search():
    if os.path.exists(fname):
        with open(fname,'r',encoding='utf-8') as file:
            lst=file.readlines()
    else:
        lst=[]
    if not lst:
        print('不存在学生信息，请先录入学生信息')
    else:
        while True:
            student_id=input('请输入查询的学生学号\n')
            if not student_id:
                print('输入的学号为空，请重新输入')
                continue
            else:
                flag=False
                for item in lst:
                    dic=dict(eval(item))
                    if dic['id']==student_id:
                        flag=True
                        print('id:', dic['id'], 'name:', dic['name'], 'chinese:', dic['chinese'], 'math:', dic['math'],
                              'english:', dic['english'], 'python:', dic['python'])
                if flag:
                    print('id为{0}的学生的信息已经输出'.format(student_id))
                else:
                    print('没有找到id为{0}的学生'.format(student_id))
                answer=input('还需要继续查询吗？？？y/n\n')
                if answer=='y':
                    continue
                else:
                    anwer=input('确定不查询了吗？？？？y/n\n')
                    if answer=='y':
                        break
                    else:
                        continue
def sort():
    if os.path.exists(fname):#判断文件是否存在
        with open(fname,'r',encoding='utf-8') as file:
            lst=file.readlines()
            student_list=[]
            for item in lst:
                dic=dict(eval(item))
                student_list.append(dic)
            print('============排序之前的学生信息============')
            show()
            while True:
                try:
                    x = int(input('请选择排序方式，0表示升序，1表示降序\n'))
                except:
                    print('输入有误，请重新输入')
                    continue
                else:
                    break
            if x==0:
                while True:
                    try:
                        select_one = int(input(
                            '请输入,1表示按照chinese排序，2表示按照math进行排序，3表示按照english进行排序，4按照python成绩进行排序，0表示按照总成绩进行排序\n'))
                    except:
                        print('输入有误，请重新输入')
                        continue
                    else:
                        break
                if select_one==1:#按照chinese成绩进行排序
                    for i in range(len(student_list)-1):
                        for j in range(i+1,len(student_list)):
                            if student_list[i]['chinese']>student_list[j]['chinese']:
                                t=student_list[i]
                                student_list[i]=student_list[j]
                                student_list[j]=t
                elif select_one==2:#按照math成绩进行排序
                    for i in range(len(student_list) - 1):
                        for j in range(i + 1, len(student_list)):
                            if student_list[i]['math'] > student_list[j]['math']:
                                t = student_list[i]
                                student_list[i] = student_list[j]
                                student_list[j] = t
                elif select_one==3:#按照english成绩进行排序
                    for i in range(len(student_list) - 1):
                        for j in range(i + 1, len(student_list)):
                            if student_list[i]['english'] > student_list[j]['english']:
                                t = student_list[i]
                                student_list[i] = student_list[j]
                                student_list[j] = t
                elif select_one==0:#按照总成绩进行排序
                    for i in range(len(student_list) - 1):
                        for j in range(i + 1, len(student_list)):
                            if (student_list[i]['english']+student_list[i]['math']+student_list[i]['chinese']+student_list[i]['python']) > (student_list[j]['english']+student_list[j]['math']+student_list[j]['chinese']+student_list[j]['python']):
                                t = student_list[i]
                                student_list[i] = student_list[j]
                                student_list[j] = t
                elif select_one==4:#按照python成绩进行排序
                    for i in range(len(student_list) - 1):
                        for j in range(i + 1, len(student_list)):
                            if student_list[i]['python'] > student_list[j]['python']:
                                t = student_list[i]
                                student_list[i] = student_list[j]
                                student_list[j] = t
                with open(fname,'w',encoding='utf-8') as wfile:#以只写的方式打开文件，将排序好的学生信息写入文件中
                    for i in student_list:
                        wfile.write(str(i)+'\n')
                print('==========排序之后的学生信息===========')
                show()
            elif x==1:
                while True:
                    try:
                        select_one = int(input(
                            '请输入，1表示按照chinese成绩排序，2表示按照math成绩进行排序，3表示按照english成绩进行排序，4表示按照python成绩进行排序，0表示按照总成绩进行排序\n'))
                    except:
                        print('输入有误，请重新输入')
                        continue
                    else:
                        break
                if select_one == 1:#按照chinese成绩进行降序
                    for i in range(len(student_list) - 1):
                        for j in range(i + 1, len(student_list)):
                            if student_list[i]['chinese'] < student_list[j]['chinese']:
                                t = student_list[i]
                                student_list[i] = student_list[j]
                                student_list[j] = t
                elif select_one == 2:#按照math成绩进行降序
                    for i in range(len(student_list) - 1):
                        for j in range(i + 1, len(student_list)):
                            if student_list[i]['math'] < student_list[j]['math']:
                                t = student_list[i]
                                student_list[i] = student_list[j]
                                student_list[j] = t
                elif select_one == 3:#按照english成绩进行降序
                    for i in range(len(student_list) - 1):
                        for j in range(i + 1, len(student_list)):
                            if student_list[i]['english'] < student_list[j]['english']:
                                t = student_list[i]
                                student_list[i] = student_list[j]
                                student_list[j] = t
                elif select_one ==0:#按照总成绩进行排序
                    for i in range(len(student_list) - 1):
                        for j in range(i + 1, len(student_list)):
                            if (student_list[i]['english'] + student_list[i]['math'] + student_list[i]['chinese'] +
                                student_list[i]['python']) < (
                                    student_list[j]['english'] + student_list[j]['math'] + student_list[j]['chinese'] +
                                    student_list[j]['python']):
                                t = student_list[i]
                                student_list[i] = student_list[j]
                                student_list[j] = t
                elif select_one ==4:#按照python成绩进行排序
                    for i in range(len(student_list) - 1):
                        for j in range(i + 1, len(student_list)):
                            if student_list[i]['python'] < student_list[j]['python']:
                                t = student_list[i]
                                student_list[i] = student_list[j]
                                student_list[j] = t
                with open(fname,'w',encoding='utf-8') as wfile:#以只写的方式打开文件，覆盖之前的内容，将排序好的学生信息写入到文件中
                    for i in student_list:
                        wfile.write(str(i)+'\n')
                print('=============排序之后的学生信息=============')
                show()
    else:
        print('暂未录入数据信息，请先录入数据信息')
        return
def total():
    if os.path.exists(fname):
        with open(fname,'r',encoding='utf-8') as file:
            lst=file.readlines()
            if not lst:
                print('学生的个数为0，暂未录入学生信息')
            else:
                print('学生的个数为{0}'.format(len(lst)))
    else:
        print('学生个数为0，请先录入学生信息')
        return
def show():
    if os.path.exists(fname):
        with open(fname,'r',encoding='utf-8') as rfile:
            lst=rfile.readlines()
            for item in lst:
                dic=dict(eval(item))
                print('id:', dic['id'], 'name:', dic['name'], 'chinese:', dic['chinese'], 'math:', dic['math'],
                      'english:', dic['english'], 'python:', dic['python'],'总成绩',dic['chinese']+dic['math']+dic['english']+dic['python'])
    else:
        print('文件中没有任何数据信息!!!')
if __name__ == '__main__':
    main()
