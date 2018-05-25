#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QListWidget을 사용하여 아이템을 표시

__author__ = "Deokyu Lim <hong18s@gmail.com>"

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtCore import QVariant
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle("QTreeWidget")
        self.setFixedWidth(210)
        self.setFixedHeight(150)

        # QTreeView 생성 및 설정
        self.viewer = QListWidget(self)
        item = QListWidgetItem()
        item.setText( "Fruit")
        self.viewer.addItem(item)
        item = QListWidgetItem()
        item.setText("Vegetable")
        self.viewer.addItem(item)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())