from configparser import ConfigParser
import os
import sys
def ID():
    cf = ConfigParser()
    id_path = os.path.join(os.getcwd(), "ID.ini")  # 获取当前目录并修改为配置文件目录
    # print(id_path)
    if not os.path.isfile(id_path):  # 若配置文件不存在
        file = open("ID.ini", 'w')
        cf.read(id_path, encoding="utf-8")  # 读取配置文件
        cf.add_section("dingtalk")
        cf.write(open(id_path, "a"))
        list = [';机器人的wehook地址', ';机器人的加签密钥，如果没有使用加签此项留空', ';机器人初始化方法，只能填1，2，3。',
                ';1为通常初始化方法，2为勾选“加签”选项时使用的方法，3为设置消息链接在PC端侧边栏打开（v1.5以上新功能）']
        for i in range(0, 4):
            file.write(list[i])
            file.write('\n')
        file.close()
        cf.set("dingtalk", "wehook", "")
        cf.set("dingtalk", "secret", "")
        cf.set("dingtalk", "type", "")
        cf.write(open(id_path, "a"))
        print("配置文件成功释放，请填写ID.ini,并重启程序")
        sys.exit()