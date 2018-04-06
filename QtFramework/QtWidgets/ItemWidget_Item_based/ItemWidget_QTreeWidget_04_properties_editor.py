#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QTreeWidget을 사용하여 아이템을 표시

__author__ = "Deokyu Lim <hong18s@gmail.com>"

from collections import defaultdict

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QTreeWidget
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import qDebug


class Properties(QObject):
    def __init__(self, widget: QTreeWidget):
        super(Properties, self).__init__()
        self.root = widget.invisibleRootItem()
        self.data = {
            "metadata": {
                "version": "1.0.0",
                "related_date": {
                    "created": 1520413079,
                    "last_modified": 1520413079},
                "related_people": {
                    "author": {
                        "name": "Raven",
                        "email": "hong18s@gmail.net"
                    },
                    "last_modified_by": {
                        "name": "Deokyu",
                        "emil": "hong18s@gmail.com"
                    }
                },
                "comment": "PyQt TreeWidget Example"
            },
        }

    def recursive_set_item_field(self, parent: QTreeWidgetItem, data, depth=0):
        for d in list(data.keys()):
            item = QTreeWidgetItem()
            item.setText(0, d)
            if isinstance(data[d], dict):
                self.recursive_set_item_field(item, data[d], depth+1)
            elif isinstance(data[d], list):
                pass
            else:
                item.setText(1, str(data[d]))
            parent.addChild(item)
        return


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle("QTreeWidget Example")
        box = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(box)

        # QTreeView 생성 및 설정
        self.tw = QTreeWidget(self)
        box.addWidget(self.tw)
        self.props = Properties(self.tw)
        self.tw.setColumnCount(2)
        self.tw.setHeaderLabels(["Properties", "Value"])

        self.props.recursive_set_item_field(
            self.props.root, self.props.data)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
