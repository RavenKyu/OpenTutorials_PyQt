#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# QPixmap을 Base64로 변환

import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QByteArray
from PyQt5.QtCore import QBuffer


__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.init_ui()

    def init_ui(self):
        self.setMinimumWidth(320)
        self.setMinimumHeight(240)
        lb = QLabel()
        te = QTextEdit()
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        layout.addWidget(lb)
        layout.addWidget(te)
        self.setLayout(layout)

        # 사용할 그림 설정
        pixmap = QPixmap("apple.jpg")
        pixmap = pixmap.scaledToHeight(100)  # 사이즈가 조정
        lb.setPixmap(pixmap)

        # PNG 포맷 및 Base64로 변환
        image: QImage = pixmap.toImage()
        data = QByteArray()
        buffer = QBuffer(data)
        image.save(buffer, 'PNG')

        te.setText(str(data.toBase64()))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    exit(app.exec_())