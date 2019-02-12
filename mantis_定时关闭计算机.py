import os
import time
import tkinter
import threading


# 设置倒计时数秒
def autoClose():
    for i in range(cd):
        lbTime["text"] = "距离关闭计算机还有{}秒".format(cd - i)
        # print("距离关闭计算机还有{}秒".format(countdown-i))
        time.sleep(1)
    root.destroy()

# 计算目前到关闭计算机的秒数，用return返回值
def countDown():

    # 每天固定17：30关机
    h1, m1, s1 = 17, 29, 60

    print(h1, m1)

    systerm_time = time.strftime("%H:%M:%S")

    print(systerm_time)

    h2 = int(systerm_time[0:2])
    m2 = int(systerm_time[3:5])
    s2 = int(systerm_time[6:8])
    print("当前系统时间为 %d 点 %d 分 %d 秒" % (h2, m2, s2))

    countdown = int((h1 + (m1 / 60) - h2 - (m2 / 60)) * 3600 + s1 - s2)

    # print(countdown)
    return countdown


# 创建应用程序窗口，设置标题和大小
root = tkinter.Tk()
root.title("关闭计算机倒计时窗口")
root["width"] = 400
root["height"] = 300

# 不允许改变窗口的大小
root.resizable(False, False)

# 创建Text组件，放置一些文字
richText = tkinter.Text(root, width=380)
richText.place(x=10, y=10, width=380, height=230)
richText.insert("0.0", "计算机关闭倒计时提示，请及时保存文件并退出应用系统")

# 显示倒计时的Label
lbTime = tkinter.Label(root, fg='red', anchor='w')
lbTime.place(x=10, y=250, width=200)

if __name__ == '__main__':

    cd = countDown()

    t = threading.Thread(target=autoClose)
    t.start()
    root.mainloop()

    # os.system("shutdown -p")  # windows下关闭计算机命令
    # os.system("shutdown -P")  # linux下关闭计算机命令

    print("计算机关闭完成")
