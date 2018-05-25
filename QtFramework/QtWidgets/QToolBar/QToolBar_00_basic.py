#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# QToolBar.

import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt


__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_window()

    def init_window(self):
        self.setMinimumWidth(320)
        self.setMinimumHeight(240)
        self.setTabPosition(Qt.RightDockWidgetArea, QTabWidget.North)

        # 중앙 위젯
        self.lb = QLabel()
        self.setCentralWidget(self.lb)
        self._init_toolbar()

    def _init_toolbar(self):
        self.toolbar = QToolBar(self)
        action_1 = QAction(self)
        action_1.setText("QAction_1")
        action_2 = QAction(self)
        action_2.setText("QAction_2")
        action_3 = QAction(self)
        action_3.setText("QAction_3")
        # triggered 는 시그널 처럼 사용할 수 있다.
        action_1.triggered.connect(lambda: self.lb.setText(action_1.text()))
        action_2.triggered.connect(lambda: self.lb.setText(action_2.text()))
        action_3.triggered.connect(lambda: self.lb.setText(action_3.text()))
        self.toolbar.addAction(action_1)
        self.toolbar.addAction(action_2)
        self.toolbar.addAction(action_3)
        self.addToolBar(self.toolbar)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    exit(app.exec_())