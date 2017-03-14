#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QListView 기본 사용법
# * QAbstractListModel 을 이용한 사용자 모델 생성
# * 수정이 가능한 모델

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtCore import QAbstractItemModel
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Model(QStandardItemModel):
	"""
	사용자 데이터 모델 설정
	[{"type":str, "objects":[str, ...]}, ...]
	위의 데이터 형식을 이용하여 서브 아이템을 가지는 모델을 생성

	"""
	def __init__(self, data):
		QStandardItemModel.__init__(self)

		d = data[0]  # Fruit
		item = QStandardItem(d["type"])
		child = QStandardItem(d["objects"][0])  # Apple
		item.appendRow(child)
		child = QStandardItem(d["objects"][1])  # Banana
		item.appendRow(child)
		self.setItem(0, 0, item)

		d = data[1]  # Vegetable
		item = QStandardItem(d["type"])
		child = QStandardItem(d["objects"][0])  # Carrot
		item.appendRow(child)
		child = QStandardItem(d["objects"][1])  # Tomato
		item.appendRow(child)
		self.setItem(1, 0, item)

		# for 문을 이용해서 작성했을 경우
		# for j, _type in enumerate(data):
		# 	item = QStandardItem(_type["type"])
		# 	for obj in _type["objects"]:
		# 		child = QStandardItem(obj)
		# 		item.appendRow(child)
		# 	self.setItem(j, 0, item)


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.setWindowTitle("ItemView QListView")
		self.setFixedWidth(210)
		self.setFixedHeight(150)

		# 데이터
		data = [
			{"type": "Fruit", "objects": ["Apple", "Banana"]},
			{"type": "Vegetable", "objects": ["Carrot", "Tomato"]},
		]
		# QTreeView 생성 및 설정
		view = QTreeView(self)
		view.setEditTriggers(QAbstractItemView.DoubleClicked)

		model = Model(data)
		view.setModel(model)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
