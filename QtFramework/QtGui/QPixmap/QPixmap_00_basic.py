#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QPixmap사용

import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.lb_1 = QLabel()
        self.init_ui()

    def init_ui(self):
        self.setMinimumWidth(320)
        self.setMinimumHeight(240)
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(layout)
        pixmap = QPixmap("apple.jpg")
        pixmap = pixmap.scaledToHeight(240)  # 사이즈가 조정
        self.lb_1.setPixmap(pixmap)

        layout.addWidget(self.lb_1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    exit(app.exec_())