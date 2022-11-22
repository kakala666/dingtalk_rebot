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
ding_talk_body=cf.get("texttalk","body")
texttalk_sleep_time=int(cf.get("texttalk","sleep_time"))
print(wehook,secret)
def start_write_homework(间隔,wehook,secret,talk_bodu):
    if __name__=='__main__':
        催 = multiprocessing.Process(target=homework.homework, args=(间隔, wehook, secret, ding_talk_body))  # 实例化进程对象
        催.start()
start_write_homework(texttalk_sleep_time,wehook,secret,ding_talk_body)