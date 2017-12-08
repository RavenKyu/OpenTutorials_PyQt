#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 사용자 정의 슬롯 생성 및 사용

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.cnt = 0
        self.lb = QLabel(str(self.cnt))
        self.pb = QPushButton("Count")

        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Custom Signal")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        # 시그널 슬롯 연결
        self.pb.clicked.connect(self.count)

        form_lbx.addWidget(self.lb)
        form_lbx.addWidget(self.pb)

    @pyqtSlot()
    def count(self):
        # pyqtSlot 데코레이터를 이용하여 메소드를 Qt Slot으로 명시해야한다.
        self.cnt += 1
        self.lb.setText(str(self.cnt))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())