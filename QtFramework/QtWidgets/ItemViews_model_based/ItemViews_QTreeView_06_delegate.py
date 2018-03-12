#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QListView 기본 사용법
# * QAbstractListModel 을 이용한 사용자 모델 생성
# * 수정이 가능한 모델

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QAbstractItemView

from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import QAbstractItemModel
from PyQt5.QtWidgets import QItemDelegate
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QStyleOptionViewItem

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class ComboBoxDelegate(QItemDelegate):
    def __init__(self, data: list):
        QItemDelegate.__init__(self)
        self.data = data

    def createEditor(
            self, parent:QWidget, option: QStyleOptionViewItem,
            idx: QModelIndex):

        combobox = QComboBox(parent)
        combobox.insertItems(0, self.data)
        combobox.currentIndexChanged.connect(self.currentIndexChanged)
        return combobox

    def setEditorData(self, editor: QWidget, idx: QModelIndex):
        # editor.blockSignas(True)
        # editor.blockSignas(False)
        return

    def setModelData(self, editor: QWidget, model: QAbstractItemModel, idx: QModelIndex):
        model.setData(idx, self.data[editor.currentIndex()])

    @pyqtSlot(int, name="currentIndexChanged")
    def current_index_changed(self, idx):
        self.commitData.emit(self.sender())


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
        self.setHeaderData(0, Qt.Horizontal, "Type")
        self.setHeaderData(1, Qt.Horizontal, "Color")

        for i, v in enumerate(data):
            item_type = data[i]['type']

            row_items = list()
            column_items = list()

            for j, x in enumerate(data[i]['objects']):
                name, color = data[i]['objects'][j]
                item = QStandardItem(item_type)
                child = QStandardItem(name)
                row_items.append(child)
                column = QStandardItem(color)
                column_items.append(column)

            item.appendRows(row_items)
            item.appendColumn(column_items)
            self.setItem(i, 0, item)



class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle("ItemView QListView")
        box = QBoxLayout(QBoxLayout.TopToBottom)

        # 데이터
        data = [
            {
                "type": "Fruit",
                "objects": [("Apple", "Red"), ("Banana", "Yellow")]},
            {
                "type": "Vegetable",
                "objects": [("Carrot", "Red"), ("Tomato", "Red")]},
        ]
        # QTreeView 생성 및 설정
        view = QTreeView(self)
        view.setEditTriggers(QAbstractItemView.DoubleClicked)
        view.setItemDelegateForColumn(1, ComboBoxDelegate(["Red", "Yellow"]))

        model = Model(data)
        view.setModel(model)

        box.addWidget(view)
        self.setLayout(box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
