#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QListView 기본 사용법
# * QAbstractListModel 을 이용한 사용자 모델 생성
# * 모양 다듬기

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QBoxLayout

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Model(QStandardItemModel):
    """
    사용자 데이터 모델 설정

    """
    def __init__(self, data):
        """
        :param data = [{"type":str, "objects":[str, ...]}, "picture":str, ...]
        """
        QStandardItemModel.__init__(self)

        # QStandardItem에 데이터를 넣고 model에 추가
        root = self.invisibleRootItem()
        root.appendRows(self.recursive_data_set(data))
        self.setItemPrototype(root)

    def recursive_data_set(self, data):
        items = list()
        for d in data:
            item = QStandardItem(d["name"])
            item.setData(d["icon"], Qt.DecorationRole)
            if d['objects']:
                item.appendRows(self.recursive_data_set(d['objects']))
            items.append(item)
        return items

    def data(self, QModelIndex, role=None):
        data = self.itemData(QModelIndex)
        if role == Qt.DisplayRole:
            ret = data[role]
        elif role in data and role == Qt.DecorationRole:
            ret = QPixmap(data[role]).scaledToHeight(25)
        else:
            ret = QVariant()
        return ret


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle("ItemView QTreeView")
        self.setFixedWidth(310)
        self.setFixedHeight(200)

        data = [
            {"name": "Mouse Action", "icon": "assets/mouse.png", "objects": [
                {"name": "Click", "icon": "assets/network.png", "objects": None},
                {"name": "Double Click", "icon": "assets/mail.png", "objects": None},
            ]},
            {"name": "Keyboard", "icon": "assets/keyboard.png", "objects": [
                {"name": "Send Hotkey", "icon": "assets/earth.png", "objects": None},
                {"name": "Type", "icon": "assets/folder.png", "objects": None},
            ]}
        ]

        self.layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.layout)

        # QTreeView 생성 및 설정
        view = QTreeView(self)
        # QTreeView 스타일시트 설정
        view.setStyleSheet(open("./ItemViews_QTreeView_03_style.css").read())
        view.setAlternatingRowColors(True)  # 라인별 교차색
        self.model = Model(data)
        view.setModel(self.model)
        self.layout.addWidget(view)

        # 그림을 띄울 QLabel 생성
        self.lb = QLabel()
        self.lb.setFixedSize(50, 50)
        self.layout.addWidget(self.lb)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
