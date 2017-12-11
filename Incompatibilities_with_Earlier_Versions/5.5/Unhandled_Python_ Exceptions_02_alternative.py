#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# C++ 로 바인딩된 코드 사용중 에러 발생시 Traceback 안되는 상황 재현 및 처리
# 메세지박스를 이용하여 에러 상황 전달

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
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

def exception_hook(t, val, tb):
    QMessageBox.critical(None, "An exception was raised", "Exception type: {}".format(t))
    old_exception_hook(t, val, tb)

if __name__ == "__main__":
    # 예외 훅을 재설정.
    old_exception_hook = sys.excepthook
    sys.excepthook = exception_hook

    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
