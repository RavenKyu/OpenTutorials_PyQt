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
            item = QStandardItem(d["name"])
            item.setData(d["image"], Qt.DecorationRole)
            self.setItem(i, 0, item)

    def data(self, QModelIndex, role=None):
        data = self.itemData(QModelIndex)
        if role == Qt.DisplayRole:
            return "%s" % (data[role])
        elif role in data and role == Qt.DecorationRole:
            return QPixmap(data[role]).scaledToHeight(25)
        elif role == Qt.UserRole:
            print(data[role])
        return QVariant()


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("QComboBox Widget")
        self.setMinimumWidth(150)
        form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
        self.setLayout(form_lbx)

        data = [
            {"name": "Apple", "image": IMAGE_PATH + "apple.jpg"},
            {"name": "Banana", "image": IMAGE_PATH + "banana.jpg"}
        ]
        model = UserModel(data)

        lb = QLabel()

        qb = QComboBox()
        qb.setModel(model)
        qb.currentTextChanged.connect(lb.setText)  # 현재 인덱스의 데이터가 바뀔 때

        form_lbx.addWidget(qb)
        form_lbx.addWidget(lb)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
