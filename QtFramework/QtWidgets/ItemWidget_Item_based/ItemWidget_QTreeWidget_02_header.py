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
        self.setWindowTitle("QTreeWidget Column")
        self.setFixedWidth(210)
        self.setFixedHeight(150)

        # 데이터
        data = [
            {"type": "Fruit",
             "objects": [("Apple", "Red"), ("Banana", "Yellow")]},
            {"type": "Vegetable",
             "objects": [("Carrot", "Red"), ("Tomato", "Red")]},
        ]
        # QTreeView 생성 및 설정
        self.tw = QTreeWidget(self)
        self.tw.setColumnCount(2)
        self.tw.setHeaderLabels(["Type", "Color"])

        for d in data:
            parent = self.add_tree_root(d['type'], "")
            for child in d['objects']:
                self.add_tree_child(parent, *child)

    def add_tree_root(self, name:str, description:str):
        item = QTreeWidgetItem(self.tw)
        item.setText(0, name)
        item.setText(1, description)
        return item

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