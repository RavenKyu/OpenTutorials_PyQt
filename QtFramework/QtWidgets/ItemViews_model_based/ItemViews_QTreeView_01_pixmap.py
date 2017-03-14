#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QListView 기본 사용법
# * QAbstractListModel 을 이용한 사용자 모델 생성
# * 수정이 가능한 모델

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Model(QStandardItemModel):
	"""
	사용자 데이터 모델 설정
	[{"type":str, "objects":[str, ...]}, ...]

	"""
	def __init__(self, data):
		QStandardItemModel.__init__(self)
		self._data = data
		for j, d in enumerate(data):
			item = QStandardItem(d["type"])
			for obj in d["objects"]:
				child = QStandardItem(obj)
				child.setData(d["picture"], Qt.DecorationRole)  # Role 이름의 키 값을 가지게 될 데이터 정의
				item.appendRow(child)
			self.setItem(j, 0, item)

	def data(self, QModelIndex, role=None):
		# itemData에 인자값으로 받은 QModelIndex를 넣어주면 사전형태의 데이터 값을 돌려준다.
		data = self.itemData(QModelIndex)

		if role == Qt.DisplayRole:
			ret = data[role]
		elif role in data and role == Qt.DecorationRole:
			ret = QPixmap(data[role]).scaledToHeight(25)
		else:
			ret = QVariant()
		return ret


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.setWindowTitle("ItemView QListView")
		self.setFixedWidth(210)
		self.setFixedHeight(150)

		data = [
			{"type": "Sword", "objects": ["Long Sword", "Short Sword"], "picture": "sword.png"},
			{"type": "Shield", "objects": ["Wood Shield", "iron Shied"], "picture": "shield.png"},
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
