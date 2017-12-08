#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 실행상태바의 기본 사용

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QScrollBar
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Hello World")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        pgsb = QProgressBar()
        vscrb = QScrollBar(orientation=Qt.Horizontal)
        vscrb.setRange(0, 100)
        vscrb.valueChanged.connect(pgsb.setValue)

        form_lbx.addWidget(pgsb)
        form_lbx.addWidget(vscrb)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())