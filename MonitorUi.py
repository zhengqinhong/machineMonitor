# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MonitorUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import re

from PyQt5.QtGui import QImage

from RTSCapture import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QByteArray,QTimer
import time
import numpy as np

class AutoMonitor(QtWidgets.QMainWindow):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.dir = 'C:/'
        self.threshold = 30
        self.my_rtsp = RTSCapture()
        self.setupUi(self)
        self.textEdit.setText(self.dir)
        self.ImageStart.setEnabled(True)
        self.ImageStop.setEnabled(False)
        self.ProcessStart.setEnabled(False)
        self.ProcessStop.setEnabled(False)
        self.thread_run_flag = 0
        self.thread_start_flag = 0
        self.thread_frame = None
        self.widget = 960
        self.height = 540
        self.show_image = QtWidgets.QLabel()
        self.init()

    def __del__(self):
        pass

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1276, 800)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(800, 0, 471, 800))
        self.widget.setObjectName("widget")
        self.ProcessStart = QtWidgets.QPushButton(self.widget)
        self.ProcessStart.setGeometry(QtCore.QRect(30, 710, 93, 28))
        self.ProcessStart.setObjectName("ProcessStart")
        self.ProcessStop = QtWidgets.QPushButton(self.widget)
        self.ProcessStop.setGeometry(QtCore.QRect(170, 710, 93, 28))
        self.ProcessStop.setObjectName("ProcessStop")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(10, 290, 441, 261))
        self.widget_2.setObjectName("widget_2")
        self.area1_y = QtWidgets.QLineEdit(self.widget_2)
        self.area1_y.setGeometry(QtCore.QRect(150, 50, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area1_y.setFont(font)
        self.area1_y.setText("")
        self.area1_y.setReadOnly(False)
        self.area1_y.setObjectName("area1_y")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(50, 50, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.area1 = QtWidgets.QRadioButton(self.widget_2)
        self.area1.setGeometry(QtCore.QRect(20, 60, 21, 16))
        self.area1.setText("")
        self.area1.setObjectName("area1")
        self.area1_x = QtWidgets.QLineEdit(self.widget_2)
        self.area1_x.setGeometry(QtCore.QRect(70, 50, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area1_x.setFont(font)
        self.area1_x.setText("")
        self.area1_x.setReadOnly(False)
        self.area1_x.setObjectName("area1_x")
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setGeometry(QtCore.QRect(130, 50, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.area2_y = QtWidgets.QLineEdit(self.widget_2)
        self.area2_y.setGeometry(QtCore.QRect(150, 100, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area2_y.setFont(font)
        self.area2_y.setText("")
        self.area2_y.setReadOnly(False)
        self.area2_y.setObjectName("area2_y")
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setGeometry(QtCore.QRect(50, 100, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.area2 = QtWidgets.QRadioButton(self.widget_2)
        self.area2.setGeometry(QtCore.QRect(20, 110, 21, 16))
        self.area2.setText("")
        self.area2.setObjectName("area2")
        self.area2_x = QtWidgets.QLineEdit(self.widget_2)
        self.area2_x.setGeometry(QtCore.QRect(70, 100, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area2_x.setFont(font)
        self.area2_x.setText("")
        self.area2_x.setReadOnly(False)
        self.area2_x.setObjectName("area2_x")
        self.label_14 = QtWidgets.QLabel(self.widget_2)
        self.label_14.setGeometry(QtCore.QRect(130, 100, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.area3_y = QtWidgets.QLineEdit(self.widget_2)
        self.area3_y.setGeometry(QtCore.QRect(150, 150, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area3_y.setFont(font)
        self.area3_y.setText("")
        self.area3_y.setReadOnly(False)
        self.area3_y.setObjectName("area3_y")
        self.label_15 = QtWidgets.QLabel(self.widget_2)
        self.label_15.setGeometry(QtCore.QRect(50, 150, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.area3 = QtWidgets.QRadioButton(self.widget_2)
        self.area3.setGeometry(QtCore.QRect(20, 160, 21, 16))
        self.area3.setText("")
        self.area3.setObjectName("area3")
        self.area3_x = QtWidgets.QLineEdit(self.widget_2)
        self.area3_x.setGeometry(QtCore.QRect(70, 150, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area3_x.setFont(font)
        self.area3_x.setText("")
        self.area3_x.setReadOnly(False)
        self.area3_x.setObjectName("area3_x")
        self.label_16 = QtWidgets.QLabel(self.widget_2)
        self.label_16.setGeometry(QtCore.QRect(130, 150, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.area4_y = QtWidgets.QLineEdit(self.widget_2)
        self.area4_y.setGeometry(QtCore.QRect(150, 200, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area4_y.setFont(font)
        self.area4_y.setText("")
        self.area4_y.setReadOnly(False)
        self.area4_y.setObjectName("area4_y")
        self.label_17 = QtWidgets.QLabel(self.widget_2)
        self.label_17.setGeometry(QtCore.QRect(50, 200, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.area4 = QtWidgets.QRadioButton(self.widget_2)
        self.area4.setGeometry(QtCore.QRect(20, 210, 21, 16))
        self.area4.setText("")
        self.area4.setObjectName("area4")
        self.area4_x = QtWidgets.QLineEdit(self.widget_2)
        self.area4_x.setGeometry(QtCore.QRect(70, 200, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area4_x.setFont(font)
        self.area4_x.setText("")
        self.area4_x.setReadOnly(False)
        self.area4_x.setObjectName("area4_x")
        self.label_18 = QtWidgets.QLabel(self.widget_2)
        self.label_18.setGeometry(QtCore.QRect(130, 200, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.area1_w = QtWidgets.QLineEdit(self.widget_2)
        self.area1_w.setGeometry(QtCore.QRect(270, 50, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area1_w.setFont(font)
        self.area1_w.setText("")
        self.area1_w.setReadOnly(False)
        self.area1_w.setObjectName("area1_w")
        self.label_19 = QtWidgets.QLabel(self.widget_2)
        self.label_19.setGeometry(QtCore.QRect(330, 50, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.area1_h = QtWidgets.QLineEdit(self.widget_2)
        self.area1_h.setGeometry(QtCore.QRect(350, 50, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area1_h.setFont(font)
        self.area1_h.setText("")
        self.area1_h.setReadOnly(False)
        self.area1_h.setObjectName("area1_h")
        self.label_20 = QtWidgets.QLabel(self.widget_2)
        self.label_20.setGeometry(QtCore.QRect(250, 50, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.widget_2)
        self.label_21.setGeometry(QtCore.QRect(250, 100, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.area2_h = QtWidgets.QLineEdit(self.widget_2)
        self.area2_h.setGeometry(QtCore.QRect(350, 100, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area2_h.setFont(font)
        self.area2_h.setText("")
        self.area2_h.setReadOnly(False)
        self.area2_h.setObjectName("area2_h")
        self.area2_w = QtWidgets.QLineEdit(self.widget_2)
        self.area2_w.setGeometry(QtCore.QRect(270, 100, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area2_w.setFont(font)
        self.area2_w.setText("")
        self.area2_w.setReadOnly(False)
        self.area2_w.setObjectName("area2_w")
        self.label_22 = QtWidgets.QLabel(self.widget_2)
        self.label_22.setGeometry(QtCore.QRect(330, 100, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.widget_2)
        self.label_23.setGeometry(QtCore.QRect(250, 150, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.area3_h = QtWidgets.QLineEdit(self.widget_2)
        self.area3_h.setGeometry(QtCore.QRect(350, 150, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area3_h.setFont(font)
        self.area3_h.setText("")
        self.area3_h.setReadOnly(False)
        self.area3_h.setObjectName("area3_h")
        self.area3_w = QtWidgets.QLineEdit(self.widget_2)
        self.area3_w.setGeometry(QtCore.QRect(270, 150, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area3_w.setFont(font)
        self.area3_w.setText("")
        self.area3_w.setReadOnly(False)
        self.area3_w.setObjectName("area3_w")
        self.label_24 = QtWidgets.QLabel(self.widget_2)
        self.label_24.setGeometry(QtCore.QRect(330, 150, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.widget_2)
        self.label_25.setGeometry(QtCore.QRect(250, 200, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.area4_h = QtWidgets.QLineEdit(self.widget_2)
        self.area4_h.setGeometry(QtCore.QRect(350, 200, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area4_h.setFont(font)
        self.area4_h.setText("")
        self.area4_h.setReadOnly(False)
        self.area4_h.setObjectName("area4_h")
        self.area4_w = QtWidgets.QLineEdit(self.widget_2)
        self.area4_w.setGeometry(QtCore.QRect(270, 200, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area4_w.setFont(font)
        self.area4_w.setText("")
        self.area4_w.setReadOnly(False)
        self.area4_w.setObjectName("area4_w")
        self.label_26 = QtWidgets.QLabel(self.widget_2)
        self.label_26.setGeometry(QtCore.QRect(330, 200, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.area_num = QtWidgets.QComboBox(self.widget_2)
        self.area_num.setGeometry(QtCore.QRect(100, 10, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.area_num.setFont(font)
        self.area_num.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.area_num.setObjectName("area_num")
        self.area_num.addItem("")
        self.area_num.addItem("")
        self.area_num.addItem("")
        self.area_num.addItem("")
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 71, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_31 = QtWidgets.QLabel(self.widget_2)
        self.label_31.setGeometry(QtCore.QRect(80, 260, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(10, 110, 341, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(30, 80, 261, 61))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_savePath = QtWidgets.QPushButton(self.frame)
        self.pushButton_savePath.setGeometry(QtCore.QRect(30, 40, 111, 31))
        self.pushButton_savePath.setObjectName("pushButton_savePath")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(30, 10, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(20, 10, 251, 91))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_30 = QtWidgets.QLabel(self.frame_2)
        self.label_30.setGeometry(QtCore.QRect(40, 50, 51, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.lineEdit_IP = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_IP.setGeometry(QtCore.QRect(90, 10, 151, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit_IP.setFont(font)
        self.lineEdit_IP.setReadOnly(False)
        self.lineEdit_IP.setObjectName("lineEdit_IP")
        self.label_27 = QtWidgets.QLabel(self.frame_2)
        self.label_27.setGeometry(QtCore.QRect(10, 10, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.lineEdit_threshold = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_threshold.setGeometry(QtCore.QRect(110, 50, 51, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit_threshold.setFont(font)
        self.lineEdit_threshold.setText("")
        self.lineEdit_threshold.setReadOnly(False)
        self.lineEdit_threshold.setObjectName("lineEdit_threshold")
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setGeometry(QtCore.QRect(10, 570, 281, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_Resolution = QtWidgets.QLabel(self.frame_3)
        self.label_Resolution.setGeometry(QtCore.QRect(10, 0, 81, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_Resolution.setFont(font)
        self.label_Resolution.setObjectName("label_Resolution")
        self.lineEdit_Resolution_w = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_Resolution_w.setGeometry(QtCore.QRect(110, 0, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit_Resolution_w.setFont(font)
        self.lineEdit_Resolution_w.setReadOnly(True)
        self.lineEdit_Resolution_w.setObjectName("lineEdit_Resolution_w")
        self.label_28 = QtWidgets.QLabel(self.frame_3)
        self.label_28.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.label_28.setObjectName("label_28")
        self.error_num = QtWidgets.QLabel(self.frame_3)
        self.error_num.setGeometry(QtCore.QRect(80, 50, 72, 20))
        self.error_num.setObjectName("error_num")
        self.lineEdit_Resolution_h = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_Resolution_h.setGeometry(QtCore.QRect(190, 0, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit_Resolution_h.setFont(font)
        self.lineEdit_Resolution_h.setReadOnly(True)
        self.lineEdit_Resolution_h.setObjectName("lineEdit_Resolution_h")
        self.label_32 = QtWidgets.QLabel(self.frame_3)
        self.label_32.setGeometry(QtCore.QRect(90, 0, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame_3)
        self.label_33.setGeometry(QtCore.QRect(170, 0, 16, 30))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.ImageStart = QtWidgets.QPushButton(self.widget)
        self.ImageStart.setGeometry(QtCore.QRect(360, 10, 93, 28))
        self.ImageStart.setObjectName("ImageStart")
        self.ImageStop = QtWidgets.QPushButton(self.widget)
        self.ImageStop.setGeometry(QtCore.QRect(360, 50, 93, 28))
        self.ImageStop.setObjectName("ImageStop")
        self.openGLWidget = QtWidgets.QOpenGLWidget(Form)
        self.openGLWidget.setGeometry(QtCore.QRect(0, 0, 800, 800))
        self.openGLWidget.setObjectName("openGLWidget")
        self.label_10.setBuddy(self.area1_x)
        self.label_11.setBuddy(self.area1_y)
        self.label_13.setBuddy(self.area2_x)
        self.label_14.setBuddy(self.area2_y)
        self.label_15.setBuddy(self.area3_x)
        self.label_16.setBuddy(self.area3_y)
        self.label_17.setBuddy(self.area4_x)
        self.label_18.setBuddy(self.area4_y)
        self.label_19.setBuddy(self.area1_h)
        self.label_20.setBuddy(self.area1_w)
        self.label_21.setBuddy(self.area2_w)
        self.label_22.setBuddy(self.area2_h)
        self.label_23.setBuddy(self.area3_w)
        self.label_24.setBuddy(self.area3_h)
        self.label_25.setBuddy(self.area4_w)
        self.label_26.setBuddy(self.area4_h)
        self.label_12.setBuddy(self.area_num)
        self.label_31.setBuddy(self.area4_x)
        self.label_29.setBuddy(self.area_num)
        self.label_32.setBuddy(self.area4_x)
        self.label_33.setBuddy(self.area4_x)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Capture"))
        self.ProcessStart.setText(_translate("Form", "??????"))
        self.ProcessStop.setText(_translate("Form", "??????"))
        self.label_10.setText(_translate("Form", "x:"))
        self.label_11.setText(_translate("Form", "y:"))
        self.label_13.setText(_translate("Form", "x:"))
        self.label_14.setText(_translate("Form", "y:"))
        self.label_15.setText(_translate("Form", "x:"))
        self.label_16.setText(_translate("Form", "y:"))
        self.label_17.setText(_translate("Form", "x:"))
        self.label_18.setText(_translate("Form", "y:"))
        self.label_19.setText(_translate("Form", "h:"))
        self.label_20.setText(_translate("Form", "w:"))
        self.label_21.setText(_translate("Form", "w:"))
        self.label_22.setText(_translate("Form", "h:"))
        self.label_23.setText(_translate("Form", "w:"))
        self.label_24.setText(_translate("Form", "h:"))
        self.label_25.setText(_translate("Form", "w:"))
        self.label_26.setText(_translate("Form", "h:"))
        self.area_num.setItemText(0, _translate("Form", "1"))
        self.area_num.setItemText(1, _translate("Form", "2"))
        self.area_num.setItemText(2, _translate("Form", "3"))
        self.area_num.setItemText(3, _translate("Form", "4"))
        self.label_12.setText(_translate("Form", "???????????????"))
        self.label_31.setText(_translate("Form", "x:"))
        self.pushButton_savePath.setText(_translate("Form", "Open Save Path"))
        self.label_29.setText(_translate("Form", "???????????????"))
        self.label_30.setText(_translate("Form", "?????????"))
        self.label_27.setText(_translate("Form", "???????????????"))
        self.label_Resolution.setText(_translate("Form", "Resolution"))
        self.label_28.setText(_translate("Form", "???????????????"))
        self.error_num.setText(_translate("Form", "0???"))
        self.label_32.setText(_translate("Form", "w:"))
        self.label_33.setText(_translate("Form", "h:"))
        self.ImageStart.setText(_translate("Form", "??????"))
        self.ImageStop.setText(_translate("Form", "??????"))

    def init(self):
        self.lineEdit_IP.setText("192.168.0.156")
        self.lineEdit_threshold.setText("30")
        self.pushButton_savePath.clicked.connect(self.bindList)
        self.ProcessStart.clicked.connect(self.startMonitor)
        self.ProcessStop.clicked.connect(self.stopMonitor)
        self.ImageStart.clicked.connect(self.startFrame)
        self.ImageStop.clicked.connect(self.stopFrame)

    def bindList(self):
        self.dir = QFileDialog().getExistingDirectory(None, "Select a directory", self.dir)
        self.textEdit.setText(self.dir)

    def convertCv2ToQimage(self, cv2image):
        # width = cv2image.shape[1]
        # height = cv2image.shape[0]
        return QImage(cv2image.data, self.width, self.height, self.width, QImage.Format_Grayscale8)

    def showFrame(self):
        self.cap = cv2.VideoCapture(0)  # ???????????? VideoCapture ??????
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.widget)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        #while self.thread_start_flag:
        while self.thread_run_flag:
            if self.cap.isOpened():
                cvimg = self.cap.read()
                if len(np.shape(cvimg)) == 2:
                    cvimg = cv2.cvtColor(cvimg, cv2.COLOR_GRAY2RGB)
                self.show_image.setPixmap(QtGui.QPixmap.fromImage(self.convertCv2ToQimage(cvimg)))
                # paint = QtGui.QPainter()
                # paint.begin(self.openGLWidget)
                # paint.drawImage(self.convertCv2ToQimage(cvimg))
                # paint.end()
                print("painter frame")
            else:
                time.sleep(1 * 300 / 1000.0)
                print("wait frame")
        self.cap.release()

    def startFrame(self):
        self.thread_run_flag = 1
        self.thread_frame = threading.Thread(target=self.showFrame)
        self.thread_frame.start()
        print("open cv. start recv frame")

    def stopFrame(self):
        self.thread_run_flag = 0

    def startMonitor(self):
        print("ip:"+self.lineEdit_IP.text()+"threshold:"+self.lineEdit_threshold.text())
        self.my_rtsp.create("rtsp://"+self.lineEdit_IP.text())
        print("start read rtsp")
        # self.my_rtsp.start_read()  # ???????????????????????? read_latest_frame ?????????
        print("start read rtsp &")
        self.ProcessStart.setEnabled(False)
        self.ProcessStop.setEnabled(True)

    def stopMonitor(self):
        self.ProcessStart.setEnabled(True)
        self.ProcessStop.setEnabled(False)
        self.label_32.setText(_translate("Form", "w:"))
        self.label_33.setText(_translate("Form", "h:"))
        self.ImageStart.setText(_translate("Form", "??????"))
        self.ImageStop.setText(_translate("Form", "??????"))