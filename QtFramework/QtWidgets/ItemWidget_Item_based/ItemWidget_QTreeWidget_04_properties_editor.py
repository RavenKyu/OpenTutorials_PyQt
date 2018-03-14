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


class SpinBox(QSpinBox):
    def __init__(self):
        QSpinBox.__init__(self)

    @pyqtSlot(name="getValue")
    def get_value(self):
        self.setValue(10)
        value = self.value()
        return value


class Properties(QObject):
    def __init__(self, widget: QTreeWidget):
        """

        :param widget:
        """
        super(Properties, self).__init__()
        self.root = widget.invisibleRootItem()
        # self._data = dict()
        self._data = {
            "metadata": {
                "version": "1.0.0",
                "data_type": "scenario",
                "title": "LinkedIn Test Scenario",
                "related_date": {
                    "created": 1520413079,
                    "last_modified": 1520413079},
                "related_people": {
                    "author": {
                        "name": "Raven",
                        "email": "hong18s@gmail.net"
                    },
                    "last_modified_by": {
                        "name": "Jerry",
                        "emil": "mcchae@vivans.net"
                    }
                },
                "comment": "LinkedIn RPA Scenario"
            },
        }

    def recursive_tree_item(self, item: QTreeWidgetItem, depth=0):
        # Root 아이템 부터 돌면서 아이템 내용을 Dict 형태로 생성
        for child in [item.child(i) for i in range(item.childCount())]:
            columns = [child.data(i, Qt.DisplayRole) for i in
                       range(child.columnCount())]
            # 위젯 및 체크박스 사용 여부 검사
            buf = ''
            w = child.treeWidget().itemWidget(child, 1)
            check = (child.data(1, Qt.CheckStateRole))
            if w:
                buf = w.get_value()
            if check:
                buf = ["checked", "---", "unchecked"][child.checkState(check)]
            qDebug("{} {}".format("\t" * depth, str(columns) + ' ' + str(buf)))

            if child.childCount():
                self.recursive_tree_item(child, depth + 1)

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


class ScenarioProperties(Properties):
    def __init__(self, widget):
        super(ScenarioProperties, self).__init__(widget)


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setWindowTitle("QTreeWidget Column")
        box = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(box)

        # QTreeView 생성 및 설정
        self.tw = QTreeWidget(self)
        box.addWidget(self.tw)
        self.sc_props = ScenarioProperties(self.tw)
        self.tw.setColumnCount(2)
        self.tw.setHeaderLabels(["Properties", "Value"])

        self.sc_props.recursive_set_item_field(
            self.sc_props.root, self.sc_props._data)
        self.sc_props.recursive_tree_item(self.sc_props.root)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
