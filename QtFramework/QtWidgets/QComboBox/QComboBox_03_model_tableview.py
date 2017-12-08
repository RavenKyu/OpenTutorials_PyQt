#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QComboBox 기본 사용
# * ComboBox에 그림을 추가한다.

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QTableView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QPixmap

__author__ = "Deokyu Lim <hong18s@gmail.com>"

IMAGE_PATH = "../../../Resources/Images/"


class UserModel(QStandardItemModel):
    def __init__(self, data=None, parent=None):
        QStandardItemModel.__init__(self, parent)
        for i, d in enumerate(data):
            col_1 = QStandardItem(d["name"])
            col_2 = QStandardItem(d["image"])
            col_3 = QStandardItem(d["color"])
            self.setItem(i, 0, col_1)
            self.setItem(i, 1, col_2)
            self.setItem(i, 2, col_3)
        self.setHorizontalHeaderLabels(["Name", "Image", "Color"])

    def data(self, QModelIndex, role=None):
        data = self.itemData(QModelIndex)
        if role == Qt.DisplayRole:
            if QModelIndex.column() == 1:  # 이미지 경로는 디스플레이 되지 않게 한다.
                return QVariant()
            return data[0]
        if role == Qt.DecorationRole:
            return QPixmap(data[0]).scaledToHeight(25)
        return QVariant()


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QComboBox Widget")
        self.setMinimumWidth(350)
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        data = [
            {"name": "Apple", "image": IMAGE_PATH + "apple.jpg", "color": "Red"},
            {"name": "Banana", "image": IMAGE_PATH + "banana.jpg", "color": "Yellow"}
        ]

        model = UserModel(data)

        qb = QComboBox()
        view = QTableView()
        view.setSelectionBehavior(view.SelectRows)  # 한 줄 단위로 선택

        qb.setView(view)
        qb.setModel(model)

        form_lbx.addWidget(qb)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
