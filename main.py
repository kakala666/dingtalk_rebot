# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from configparser import ConfigParser
import os
import sys
import ID,homework
import multiprocessing
ID.ID()
cf=ConfigParser()
id_path = os.path.join(os.getcwd(), "ID.ini")  # 获取当前目录并修改为配置文件目录
cf.read(id_path)  # 读取配置文件
wehook=cf.get("dingtalk","wehook")
secret=cf.get("dingtalk","secret")
type=cf.get("dingtalk","type")
print(wehook,secret,type)
def start_write_homework(间隔,wehook,secret):
    if __name__=='__main__':
        催 = multiprocessing.Process(target=homework.homework, args=(间隔, wehook, secret))  # 实例化进程对象
        催.start()
start_write_homework(1,0,0)