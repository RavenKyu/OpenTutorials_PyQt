#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 기본 위젯을 사용하여 기본 창을 생성
# * '창 이름'을 변경한다.

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import pyqtSignal

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class MouseTracker(QThread):
    """
    마우스의 위치를 쫓기 위한 Thread
    """
    # 마우스의 위치가가 변할 경우 발생
    changed_mouse_position = pyqtSignal(tuple)

    def run(self):
        cursor = None
        while True:
            c = QCursor.pos()
            # 마우스의 위치 변화가 없으면 넘어감
            if c != cursor:
                cursor = c
                self.changed_mouse_position.emit((cursor.x(), cursor.y()))
            self.usleep(1)


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget | Qt.FramelessWindowHint)
        self.init_widget()

        self.th = MouseTracker()
        self.th.changed_mouse_position.connect(
            lambda v:
            self.label.setText(
                "{}, {}".format(*v)))
        self.th.start()

    def init_widget(self):
        self.setWindowTitle("Hello World")
        self.setGeometry(10, 10, 100, 50)
        self.label = QLabel()
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addWidget(self.label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
