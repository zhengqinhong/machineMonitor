#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author：凌云剑圣
# datetime：20210919
from PyQt5.Qt import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
import sys
from usbUi import Ui_Form
import cv2 as cv
#
#
# class ShowImage:
#
#     def __init__(self, camera_object, show_label_object):
#         self.camera_object = camera_object
#         self.show_label_object = show_label_object
#         self.frame = []  # 存图片
#         self.detectFlag = False  # 检测flag
#         self.cap = []
#         self.timer_camera = QTimer()  # 定义定时器
#
#     def open_file(self):
#         """代开文件"""
#         print('打开文件')
#         self.cap = cv.VideoCapture(self.camera_object, cv.CAP_DSHOW)
#         self.timer_camera.start(100)
#         self.timer_camera.timeout.connect(self.open_frame)
#
#     def open_frame(self):
#         if (self.cap.isOpened()):
#             self.detectFlag = True
#             ret, self.frame = self.cap.read()
#             self.read_video(ret, self.frame)
#
#     def read_video(self, ret, frame):
#         if ret:
#             src = cv.flip(frame, 1)  # 摄像头镜像翻转
#             frame = cv.cvtColor(src, cv.COLOR_BGR2RGB)
#             height, width, bytesPerComponent = frame.shape
#             bytesPerLine = bytesPerComponent * width
#             q_image = QImage(frame.data, width, height, bytesPerLine,
#                              QImage.Format_RGB888).scaled(self.show_label_object.width(),
#                                                           self.show_label_object.height())
#             self.show_label_object.setPixmap(QPixmap.fromImage(q_image))
#
#         else:
#             self.cap.release()
#             self.timer_camera.stop()  # 停止计时器
#
#     def stop_video(self):
#         """停止视频"""
#         # print('play_video')
#         if self.cap != []:
#             self.cap.release()
#             self.timer_camera.stop()  # 停止计时器
#             self.detectFlag = False
#             self.show_label_object.setText("该通道已停播~\\(^o^)/~")
#             self.show_label_object.setStyleSheet("QLabel{background:pink;}"
#                                                  "QLabel{color:rgb(100,100,100);"
#                                                  "font-size:15px;font-weight:bold;"
#                                                  "font-family:宋体;}")
#         else:
#             # QMessageBox.warning(self, "Warming", "Push the left upper corner button to Quit.",
#             #                               QMessageBox.Yes)
#             pass
#
#     def save_image(self):
#         # src = cv.flip(self.frame, 1)  # 摄像头镜像翻转
#         cv.imwrite("./camera_%s.png" % str(int(self.camera_object) + 1), self.frame)  # 保存图像
#
#
# class Window(QWidget, Ui_Form):
#
#     def __init__(self):
#         super().__init__()
#         icon = './15.png'
#         self.setWindowIcon(QIcon(icon))
#         self.setupUi(self)
#         self.save_path = None
#         self.video_obj = []
#         self.video_spinBox = 1
#
#     def open_camera(self):
#         for i in range(self.video_spinBox):
#             self.video_obj.append(ShowImage(i, getattr(self, "show_video%s" % int(i + 1))))
#         return self.video_obj
#
#     def on_click(self):
#         self.pushButton.clicked.connect(self.show_multiplexer_video)
#         self.pushButton_2.clicked.connect(self.save_multiplexer_image)
#         self.pushButton_3.clicked.connect(self.quit_obj)
#         self.pushButton_4.clicked.connect(self.stop_video)
#
#     def show_multiplexer_video(self):
#         """
#         显示多路USB摄像头图像
#         :return:
#         """
#         try:
#             for i in self.open_camera():
#                 i.open_file()
#         except Exception as e:
#             print(e)
#
#     def save_multiplexer_image(self):
#         """
#         保存多路摄像头图像
#         :return:
#         """
#         try:
#             for i in self.video_obj:
#                 if i.detectFlag:
#                     i.save_image()
#         except Exception as e:
#             print(e)
#
#     def stop_video(self):
#         """ stop"""
#         try:
#             for i in self.video_obj:
#                 if i.detectFlag:
#                     i.stop_video()
#         except Exception as e:
#             print(e)
#
#     def quit_obj(self):
#         # print('88')
#         quit()
#
#
# # 在被其他文档调用时，下面的代码不会被执行
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     window.on_click()
#     sys.exit(app.exec_())


from keras.applications.vgg16 import VGG16
from keras.layers import Input, Dense, Flatten, Conv2D, BatchNormalization, MaxPooling2D, Dropout
from keras.models import Model
import numpy as np
import load_data
import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QImage,QPixmap
import cv2
import EyeSignal


def prepare_data(file):
    X, Y = load_data.get_data(file)
    # print('total images:{0}'.format(len(X)))
    return X, Y


def predict_mean_metrics(img,dictionary):

    X = np.asarray(img, dtype=np.float32)
    X=np.expand_dims(X,0)
    X -= np.array([111.40537, 120.87209, 136.82808])
    X /= np.array([43.77899962, 43.45094616, 49.08783324])
    result = model.predict(X)
    result = np.argmax(result, axis=1)
    result=dictionary[str(result[0])]
    return result



def vgg_model():
    base_model = VGG16(include_top=False, weights=None, input_shape=(200, 400, 3))
    x = Flatten(name='flatten')(base_model.output)
    x = Dense(4096, activation='relu', name='fc1')(x)
    x = Dense(4096, activation='relu', name='fc2')(x)
    x = Dense(6, activation='softmax', name='pred')(x)
    model = Model(inputs=base_model.input, outputs=x)
    model.load_weights('./weights/checkpoint.h5', by_name=True)
    return model


def cvimg_to_qtimg(cvimg):
    height, width, depth = cvimg.shape
    cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
    cvimg = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)

    return cvimg


def show_video():
    cap = cv2.VideoCapture(0)
    h, w = 200, 400
    y_offset, x_offset = 100, 120
    ls = 1
    ui.label_2.resize(w, h)
    dictionary={'0':'accelerate','1':'decelerate','2':'turn left','3':'turn right','4':'start','5':'stop'}
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.rectangle(frame, (x_offset, y_offset), (x_offset + w, y_offset + h), (0, 0, 255), ls)
        frame_cut = frame[y_offset:y_offset + h, x_offset:x_offset + w]
        image = cvimg_to_qtimg(frame_cut)
        ui.label_2.setPixmap(QPixmap(image).scaled(ui.label_2.width(), ui.label_2.height()))
        result=predict_mean_metrics(frame_cut,dictionary)
        ui.textEdit.setText(result)
        # Display the resulting frame
        # cv2.imshow('frame', frame)
        c = cv2.waitKey(30) & 0xff
        if c == 27:
            cap.release()
            break


if __name__ == "__main__":
    model = vgg_model()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = EyeSignal.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.OpenCamera.clicked.connect(show_video)
    sys.exit(app.exec_())

