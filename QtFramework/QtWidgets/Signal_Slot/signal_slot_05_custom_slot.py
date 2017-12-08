#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 사용자 정의 슬롯이 다양한 타입의 값을 받을 수 있게 만들기

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class CustomSlider(QSlider):
    def __init__(self, *args):
        QSlider.__init__(self, *args)

    @pyqtSlot(int)
    @pyqtSlot(str)
    def setValue(self, value):
        # int형과 str형을 받을 수 있도록 데코레이터를 쌓아두었다.
        value = int(value)  # 숫자 이외의 값이 들어오면 여기서 죽게된다.
        QSlider.setValue(self, value)


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.cnt = 0
        self.le = QLineEdit()
        self.dial = QDial()
        self.sld = CustomSlider(Qt.Horizontal)

        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Custom Slot")
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        control_lbx = QBoxLayout(QBoxLayout.LeftToRight, parent=self)
        self.setLayout(form_lbx)

        self.le.setMaximumWidth(40)

        # 시그널 슬롯 연결
        self.sld.valueChanged.connect(self.valueChanged)
        self.le.textChanged.connect(self.sld.setValue)
        self.dial.valueChanged.connect(self.sld.setValue)

        form_lbx.addWidget(self.dial)
        form_lbx.addLayout(control_lbx)
        control_lbx.addWidget(self.sld)
        control_lbx.addWidget(self.le)

    @pyqtSlot(int, name="valueChanged")
    def value_changed(self, value):
        self.le.setText(str(value))
        self.dial.setValue(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())