#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QListView 기본 사용법
# * QAbstractListModel 을 이용한 사용자 모델 생성
# * 수정이 가능한 모델

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem

from PyQt5.QtCore import Qt


__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Model(QStandardItemModel):
    """
    사용자 데이터 모델 설정
    [{"type":str, "objects":[str, ...]}, ...]
    위의 데이터 형식을 이용하여 서브 아이템을 가지는 모델을 생성

    """
    def __init__(self, data):
        """
        # -- Type -- Color
        |-- item_type(Fruit)
        |   |-- name(Apple) -- color(Red)
        |   |-- name(Banana) -- color(Yellow)
        |-- item_type(
        :param data:
        """
        QStandardItemModel.__init__(self, 0, 2)

        # 하나의 아이템만 받도록 되어 있음
        self.setHeaderData(0, Qt.Horizontal, "Type")
        self.setHeaderData(1, Qt.Horizontal, "Color")

        row_items = list()
        column_items = list()
        item_type = data[0]['type']
        name, color = data[0]['objects'][0]

        item = QStandardItem(item_type)

        child = QStandardItem(name)
        row_items.append(child)
        column = QStandardItem(color)
        column_items.append(column)

        name, color = data[0]['objects'][1]
        child = QStandardItem(name)
        row_items.append(child)
        column = QStandardItem(color)
        column_items.append(column)

        item.appendRows(row_items)
        item.appendColumn(column_items)
        self.setItem(0, 0, item)


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle("ItemView QTreeView")
        self.setFixedWidth(210)
        self.setFixedHeight(150)

        # 데이터
        data = [
            {
                "type": "Fruit",
                "objects": [("Apple", "Red"), ("Banana", "Yellow")]},
        ]
        # QTreeView 생성 및 설정
        view = QTreeView(self)
        view.setEditTriggers(QAbstractItemView.DoubleClicked)

        model = Model(data)
        view.setModel(model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
