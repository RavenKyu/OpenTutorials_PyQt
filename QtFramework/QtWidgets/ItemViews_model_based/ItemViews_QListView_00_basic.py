#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QListView 기본 사용법
# * QStandardItemModel과 QStandardItem 이용

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QListView
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.setWindowTitle("ItemView QListView")
		self.setFixedHeight(100)

		fruits = ["banana", "apple", "melon", "pear"]

		view = QListView(self)
		model = QStandardItemModel()
		for f in fruits:
			model.appendRow(QStandardItem(f))
		view.setModel(model)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
