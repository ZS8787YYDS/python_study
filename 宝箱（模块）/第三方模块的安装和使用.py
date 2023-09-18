print(1)
'''
安装方法为：打开命令行窗口：pip install 模块名称
安装之后可以输入python进入交互式程序，通过import 模块名字进行导入模块 如果不报错的话，说明安装成功
'''
import schedule
import time
def job():
    print('小宝贝，别急，数三秒我们就走了哈,回家！！！！')
schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

