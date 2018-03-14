#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QTreeWidget을 사용하여 아이템을 표시

__author__ = "Deokyu Lim <hong18s@gmail.com>"

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTreeWidget
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtCore import QVariant
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle("QTreeWidget Column")
        box = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(box)

        # QTreeView 생성 및 설정
        self.tw = QTreeWidget(self)
        box.addWidget(self.tw)
        self.tw.setColumnCount(2)
        self.tw.setHeaderLabels(["Properties", "Value"])

        root_1 = QTreeWidgetItem(self.tw)
        root_1.setText(0, "Option_1")
        root_1.setText(1, "Option_1 Description")


        item_1 = QTreeWidgetItem()
        item_1.setText(0, "enabled")
        item_1.setFlags(item_1.flags() | Qt.ItemIsUserCheckable)
        item_1.setCheckState(1, Qt.Checked)
        root_1.addChild(item_1)

        item_1 = QTreeWidgetItem()
        item_1.setText(0, "height")
        root_1.addChild(item_1)
        self.tw.setItemWidget(item_1, 1, QSpinBox())

        root_2 = QTreeWidgetItem(self.tw)
        root_2.setText(0, "Option_2")
        root_2.setText(1, "Option_2 Description")

        item_2 = QTreeWidgetItem()
        item_2.setText(0, "width")
        item_2.setText(1, "300")
        root_2.addChild(item_2)

        item_2 = QTreeWidgetItem()
        item_2.setText(0, "height")
        item_2.setText(1, "200")
        root_2.addChild(item_2)


    def add_tree_child(self, parent:QTreeWidgetItem, name:str, description:str):
        item = QTreeWidgetItem()
        item.setText(0, name)
        item.setText(1, description)
        parent.addChild(item)
        return item


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())