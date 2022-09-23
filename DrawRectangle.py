import sys, math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DrawRectangle(QWidget):
    def __init__(self, parent=None):
        super(DrawRectangle, self).__init__(parent)
        self.rect = None

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.rect:
            self.drawRect(qp)
        qp.end()

    def drawRect(self, qp):
        pen = QPen(Qt.red, 1)
        qp.setPen(pen)
        qp.drawRect(*self.rect)

    def mousePressEvent(self, event):
    #    print("mouse press")
        self.rect = (event.x(), event.y(), 0, 0)

    def mouseReleaseEvent(self, event):
        pass
    #    print("mouse release")

    def mouseMoveEvent(self, event):
        start_x, start_y = self.rect[0:2]
        self.rect = (start_x, start_y, event.x() - start_x, event.y() - start_y)
        self.update()

