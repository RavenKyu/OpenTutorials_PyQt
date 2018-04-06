#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QTreeWidget을 사용하여 아이템을 표시

__author__ = "Deokyu Lim <hong18s@gmail.com>"

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTreeWidget
from PyQt5.QtCore import QVariant
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle("QTreeWidget")
        self.setFixedWidth(210)
        self.setFixedHeight(150)

        # QTreeView 생성 및 설정
        self.tw = QTreeWidget(self)
        self.tw.setColumnCount(2)
        self.tw.setHeaderLabels(["Type", "Color"])
        self.root = self.tw.invisibleRootItem()

        item = QTreeWidgetItem()
        item.setText(0, "Fruit")
        sub_item = QTreeWidgetItem()
        sub_item.setText(0, "Apple")
        sub_item.setText(1, "Red")
        item.addChild(sub_item)
        self.root.addChild(item)

        item = QTreeWidgetItem()
        item.setText(0, "Vegetable")
        sub_item = QTreeWidgetItem()
        sub_item.setText(0, "Corn")
        sub_item.setText(1, "Yellow")
        item.addChild(sub_item)
        self.root.addChild(item)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())