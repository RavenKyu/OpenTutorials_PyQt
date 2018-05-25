#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QPixmap사용

import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.lb_1 = QLabel()
        self.lb_2 = QLabel()
        self.le = QLineEdit()
        self.pb = QPushButton("Pixmap")
        self.init_ui()

    def init_ui(self):
        self.setMinimumWidth(320)
        self.setMinimumHeight(240)
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(layout)

        self.lb_1.setText("QPixmap Example")

        layout.addWidget(self.lb_1)
        layout.addWidget(self.lb_2)
        layout.addWidget(self.le)
        layout.addWidget(self.pb)

        self.le.textChanged.connect(self.lb_1.setText)
        self.pb.clicked.connect(self.save)

    def save(self):
        pixmap = QPixmap(self.lb_1.size())
        self.lb_1.render(pixmap)
        self.lb_2.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    exit(app.exec_())