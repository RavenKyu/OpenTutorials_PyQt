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
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QItemDelegate
from PyQt5.QtWidgets import QStyleOptionViewItem

from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QPainter

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QAbstractItemModel
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QVariant
from PyQt5.QtCore import QModelIndex

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class TreeItem(object):
    def __init__(self, data, parent=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []

    def appendChild(self, item):
        self.childItems.append(item)

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        return len(self.itemData)

    def data(self, column):
        try:
            return self.itemData[column]
        except IndexError:
            return None

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)

        return 0


class TreeModel(QAbstractItemModel):
    def __init__(self, data, parent=None):
        super(TreeModel, self).__init__(parent)

        self.rootItem = TreeItem(("Properties", "Value"))
        self.setupModelData(data, self.rootItem)

    def columnCount(self, parent):
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index: QModelIndex, role=None):
        if not index.isValid():
            return None

        item = index.internalPointer()
        if role == Qt.DisplayRole:
            return item.data(index.column())
        return QVariant()

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()

    def _add_item(self, item):
        row = list()
        column = list()
        for sub_item in item['objects']:
            child = QStandardItem(sub_item['name'])
            col = QStandardItem(sub_item['value'])
            col.setCheckState(Qt.Checked if sub_item['value'] else Qt.Unchecked)
            col.setData(sub_item['editor'], Qt.UserRole+1)
            row.append(child)
            column.append(col)
        return row, column

    def setupModelData(self, items, parent):
        parents = [parent]
        parents[-1].appendChild(TreeItem(["option 1", "option 1 description"], parents[-1]))
        parents[-1].childItems[-1].appendChild(
            TreeItem(["enable", "True"], parents[-1].childItems[-1]))

        parents[-1].appendChild(TreeItem(["option 2", "option 2 description"], parents[-1]))
        parents[-1].childItems[-1].appendChild(
            TreeItem(["width", "100px"], parents[-1].childItems[-1]))
        parents[-1].childItems[-1].appendChild(
            TreeItem(["height", "120px"], parents[-1].childItems[-1]))


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle("ItemView QListView")
        box = QBoxLayout(QBoxLayout.TopToBottom)

        # QTreeView 생성 및 설정
        view = QTreeView(self)
        view.setEditTriggers(QAbstractItemView.DoubleClicked)

        model = TreeModel(None)

        view.setModel(model)
        box.addWidget(view)
        self.setLayout(box)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    excepthook = sys.excepthook
    sys.excepthook = lambda t, val, tb: excepthook(t, val, tb)
    form = Form()
    form.show()
    exit(app.exec_())
