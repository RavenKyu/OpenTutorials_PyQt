#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QListView 기본 사용법
# * QAbstractListModel 을 이용한 사용자 모델 생성

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QListView
from PyQt5.QtCore import QAbstractListModel
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class UserModel(QAbstractListModel):
	def __init__(self, data=None, parent=None):
		QAbstractListModel.__init__(self, parent)
		self._data = data

	def rowCount(self, parent=None, *args, **kwargs):
		return len(self._data)

	def data(self, QModelIndex, role=None):
		item = self._data[QModelIndex.row()]

		if role == Qt.DisplayRole:
			return "%s" % (item['name'])
		elif role == Qt.DecorationRole:
			return QColor(item['color'])
		elif role == Qt.BackgroundRole:
			return QBrush(Qt.Dense7Pattern)
		elif role == Qt.ToolTipRole:
			return "Tool Tip: %s" % (item['name'])
		return QVariant()


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.setWindowTitle("ItemView QListView")
		self.setFixedWidth(210)
		self.setFixedHeight(100)

		fruits = [
			{"name": "banana", "color": "yellow", "bg_color": "yellow"},
			{"name": "apple", "color": "red", "bg_color": "red"},
			{"name": "pear", "color": "green", "bg_color": "gray"},
		]

		view = QListView(self)
		model = UserModel(fruits)
		view.setModel(model)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
