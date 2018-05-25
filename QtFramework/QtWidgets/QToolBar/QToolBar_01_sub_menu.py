#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# QToolBar.

import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication


__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.lb = QLabel()
        self.menu = QMenu(self)
        self.toolbar = QToolBar(self)
        self.tool_buttons = QToolButton(self)
        # 툴버튼이 팝업으로 메뉴를 지원할 수 있게 설정
        self.tool_buttons.setPopupMode(QToolButton.MenuButtonPopup)
        # 선택된 액션이 버튼 선택사항으로 나올 수 있게 트리거 설정 (필수)
        self.tool_buttons.triggered.connect(self.tool_buttons.setDefaultAction)

        self.init_window()
        self.init_toolbar()

    def init_window(self):
        self.setMinimumWidth(320)
        self.setMinimumHeight(240)
        self.setCentralWidget(self.lb)

    def init_toolbar(self):
        # 액션 생성
        action_1 = QAction(self)
        action_1.setText("QAction_1")
        action_1.setIcon(QIcon("assets/icon_split_horizontal.svg"))
        action_1.triggered.connect(lambda: self.lb.setText(action_1.text()))

        action_2 = QAction(self)
        action_2.setText("QAction_2")
        action_2.setIcon(QIcon("assets/icon_split_vertical.svg"))
        action_2.triggered.connect(lambda: self.lb.setText(action_2.text()))

        # 메뉴에 추가
        self.menu.addAction(action_1)
        self.menu.addAction(action_2)

        # 툴 버튼에 메뉴 설정
        self.tool_buttons.setMenu(self.menu)
        # 기본 사항으로 설정될 액션 선택 (필수)
        self.tool_buttons.setDefaultAction(action_1)
        self.toolbar.addWidget(self.tool_buttons)
        self.addToolBar(self.toolbar)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    exit(app.exec_())