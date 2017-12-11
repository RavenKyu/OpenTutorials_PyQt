#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# C++ 로 바인딩된 코드 사용중 에러 발생시 Traceback 안되는 상황 재현

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QPushButton):
    def __init__(self):
        QPushButton.__init__(self)
        self.setText("Click to raise error")
        self.clicked.connect(self.error)

    @pyqtSlot()
    def error(self):
        raise RuntimeError

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
