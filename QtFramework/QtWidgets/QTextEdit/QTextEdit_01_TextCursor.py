#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 기본 위젯을 사용하여 기본 창을 생성
# * '창 이름'을 변경한다.

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"

class StatusBar(QStatusBar):
    @pyqtSlot(QTextCursor)
    def change_cursor_info(self, data:QTextCursor):
        ss = data.selectionStart()
        se = data.selectionEnd()

        selected_info = ""
        if se - ss:
            selected_info = "{0} {1}  ".format(se - ss, "char" if (se-ss) == 1 else "chars")
        self.showMessage("{0}{1}:{2}".format(
            selected_info,
            data.blockNumber(),
            data.columnNumber())
        )


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Hello World")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        te = QTextEdit()
        sb = StatusBar()

        form_lbx.addWidget(te)
        form_lbx.addWidget(sb)

        te.cursorPositionChanged.connect(lambda: sb.change_cursor_info(te.textCursor()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
