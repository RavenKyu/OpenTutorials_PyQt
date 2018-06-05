#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 기본 위젯을 사용하여 기본 창을 생성
# * '창 이름'을 변경한다.

import sys

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QPushButton):
    def __init__(self):
        QPushButton.__init__(self)
        self.init_widget()

    def init_widget(self):
        """
        현재 위젯의 모양등을 초기화
        """
        self.setWindowTitle("Hello World")
        self.setText("Change Icon")
        self.setCheckable(True)
        self.setChecked(False)
        self.change_window_icon(self.isChecked())

        self.clicked.connect(self.change_window_icon)

    def change_window_icon(self, v):
        icon = {True: "sword.png", False: 'shield.png'}
        app.setWindowIcon(QIcon(icon[v]))
        self.setIcon(QIcon(icon[v]))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
