#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QLabel에 표현될 내용물의 위치를 결정

import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()
        self.setLayout(layout)
        pixmap = QPixmap("apple.jpg")
        pixmap = pixmap.scaledToHeight(25)  # 사이즈가 조정

        # 라벨에 출력될 내용의 정렬을 선택한다.
        # 정렬 속성은 여러개를 사용할 수 있다.

        # 가운데 정렬
        lb = QLabel()
        lb.setFixedSize(100, 100)
        lb.setStyleSheet("background-color: gray")
        lb.setPixmap(pixmap)
        lb.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(lb, 0, 0)

        # 라벨에 출력될 내용의 정렬을 선택한다.
        lb = QLabel()
        lb.setFixedSize(100, 100)
        lb.setStyleSheet("background-color: gray")
        lb.setPixmap(pixmap)
        lb.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        layout.addWidget(lb, 0, 1)

        lb = QLabel()
        lb.setFixedSize(100, 100)
        lb.setStyleSheet("background-color: gray")
        lb.setPixmap(pixmap)
        lb.setAlignment(Qt.AlignRight | Qt.AlignTop)
        layout.addWidget(lb, 0, 2)

        lb = QLabel()
        lb.setFixedSize(100, 100)
        lb.setStyleSheet("background-color: gray")
        lb.setPixmap(pixmap)
        lb.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addWidget(lb, 1, 0)

        lb = QLabel()
        lb.setFixedSize(100, 100)
        lb.setStyleSheet("background-color: gray")
        lb.setPixmap(pixmap)
        lb.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        layout.addWidget(lb, 1, 1)

        lb = QLabel()
        lb.setFixedSize(100, 100)
        lb.setStyleSheet("background-color: gray")
        lb.setPixmap(pixmap)
        lb.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(lb, 1, 2)

        lb = QLabel()
        lb.setFixedSize(100, 100)
        lb.setStyleSheet("background-color: gray")
        lb.setPixmap(pixmap)
        lb.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
        layout.addWidget(lb, 2, 0)

        lb = QLabel()
        lb.setFixedSize(100, 100)
        lb.setStyleSheet("background-color: gray")
        lb.setPixmap(pixmap)
        lb.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        layout.addWidget(lb, 2, 1)

        lb = QLabel()
        lb.setFixedSize(100, 100)
        lb.setStyleSheet("background-color: gray")
        lb.setPixmap(pixmap)
        lb.setAlignment(Qt.AlignRight | Qt.AlignBottom)
        layout.addWidget(lb, 2, 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    exit(app.exec_())