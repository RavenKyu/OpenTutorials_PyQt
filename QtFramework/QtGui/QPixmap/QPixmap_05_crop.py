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
from PyQt5.QtCore import QRect

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.init_ui()

    def init_ui(self):
        self.setMinimumWidth(320)
        self.setMinimumHeight(240)
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(layout)

        lb_1 = QLabel()
        pixmap = QPixmap("apple.jpg")
        pixmap = pixmap.scaledToHeight(240)  # 사이즈가 조정
        lb_1.setPixmap(pixmap)
        layout.addWidget(lb_1)

        # 자를 영역 선택, 복사
        rect = QRect(50, 50, 50, 50)
        cropped = pixmap.copy(rect)

        lb_2 = QLabel()
        lb_2.setPixmap(cropped)
        layout.addWidget(lb_2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    exit(app.exec_())