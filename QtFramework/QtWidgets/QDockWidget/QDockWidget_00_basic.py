#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QDockWidget 사용

import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt


__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.dock_1 = QDockWidget(self)
        self.dock_2 = QDockWidget(self)
        self.init_window()

    def init_window(self):
        # 중앙 위젯
        self.setCentralWidget(QTextEdit())

        # Dock 설정
        self.dock_1.setWindowTitle("Dock1")
        # Dock이 붙을 수 있는 구역 설정
        self.dock_1.setAllowedAreas(
            Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        # Dock의 처음 위치 설정
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_1)

        self.dock_2.setWindowTitle("Dock2")
        self.dock_2.setAllowedAreas(Qt.RightDockWidgetArea)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    exit(app.exec_())