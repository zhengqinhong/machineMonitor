#!/usr/local/bin/python3
# encodin: utf-8
# author: cx

"""经过测试 cv2.VideoCapture 的 read 函数并不能获取实时流的最新帧
而是按照内部缓冲区中顺序逐帧的读取，opencv会每过一段时间清空一次缓冲区
但是清空的时机并不是我们能够控制的，因此如果对视频帧的处理速度如果跟不上接受速度
那么每过一段时间，在播放时(imshow)时会看到画面突然花屏，甚至程序直接崩溃
在网上查了很多资料，处理方式基本是一个思想
使用一个临时缓存，可以是一个变量保存最新一帧，也可以是一个队列保存一些帧
然后开启一个线程读取最新帧保存到缓存里，用户读取的时候只返回最新的一帧
这里我是使用了一个变量保存最新帧
注意：这个处理方式只是防止处理（解码、计算或播放）速度跟不上输入速度
而导致程序崩溃或者后续视频画面花屏，在读取时还是丢弃一些视频帧
这个在高性能机器上也没啥必要 [/doge]
"""



import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QSurfaceFormat
from MonitorUi import *

if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     print("usage:")
    #     print('python3 RTSCapture.py "rtsp://xxx"')
    #     sys.exit()
    app = QtWidgets.QApplication(sys.argv)
    win = AutoMonitor()
    win.show()
    res = app.exec_()
    #sys.exit(res)

# import wmi
# info = wmi.WMI()
# wql = "Select * From Win32_USBControllerDevice"
# for item in info.query(wql):
#     a = item.Dependent.PNPClass
#     b = item.Dependent.Name.upper()
#     if (a.upper() == 'MEDIA' or a.upper() == 'CAMERA') and 'AUDIO' not in b:
#         print(item.Dependent)
#
# import cv2
# cap = cv2.VideoCapture(0)#创建一个 VideoCapture 对象
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
# flag = 1 #设置一个标志，用来输出视频信息
# num = 1 #递增，用来保存文件名
# while(cap.isOpened()):#循环读取每一帧
#     ret_flag, Vshow = cap.read() #返回两个参数，第一个是bool是否正常打开，第二个是照片数组，如果只设置一个则变成一个tumple包含bool和图片
#     cv2.imshow("Capture_Test",Vshow)  #窗口显示，显示名为 Capture_Test
#     k = cv2.waitKey(1) & 0xFF #每帧数据延时 1ms，延时不能为 0，否则读取的结果会是静态帧
#     if k == ord('s'):  #若检测到按键 ‘s'，打印字符串
#         cv2.imwrite("F://save" + str(num) + ".jpg", Vshow)
#         print(cap.get(3)); #得到长宽
#         print(cap.get(4));
#         print("success to save"+str(num)+".jpg")
#         print("-------------------------")
#         num += 1
#     elif k == ord('q'): #若检测到按键 ‘q'，退出
#         break
# cap.release() #释放摄像头