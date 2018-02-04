#!/usr/bin/env python

# 예제 내용
# * QML 을 이용한 GUI 프로그래밍
# * QML 안에서 자바스크립 사용하기

__author__ = "Deokyu Lim <hong18s@gmail.com>"

from PyQt5.QtCore import QUrl
from PyQt5.QtQuick import QQuickView
from PyQt5.QtWidgets import QApplication
import sys


class MainWindow(QQuickView):
    def __init__(self):
        super().__init__()
        self.setSource(QUrl.fromLocalFile('11-PyQt_QML_javascript_in_QML.qml'))
        self.rootContext().setContextProperty("MainWindow", self)
        self.root = self.rootObject()

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())