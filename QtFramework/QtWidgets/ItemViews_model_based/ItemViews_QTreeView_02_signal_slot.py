#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QListView 기본 사용법
# * QAbstractListModel 을 이용한 사용자 모델 생성
# * 수정이 가능한 모델

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QModelIndex


__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Model(QStandardItemModel):
	"""
	사용자 데이터 모델 설정

	"""
	def __init__(self, data):
		"""
		:param data = [{"type":str, "objects":[str, ...]}, "picture":str, ...]
		"""
		QStandardItemModel.__init__(self)
		self._data = data

		# QStandardItem에 데이터를 넣고 model에 추가
		for j, d in enumerate(data):
			item = QStandardItem(d["type"])
			for obj in d["objects"]:
				child = QStandardItem(obj)
				child.setData(d["picture"], Qt.DecorationRole)
				item.appendRow(child)
			self.setItem(j, 0, item)

	def data(self, QModelIndex, role=None):
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
		self.setFixedWidth(310)
		self.setFixedHeight(200)

		data = [
			{"type": "Sword", "objects": ["Long Sword", "Short Sword"], "picture": "sword.png"},
			{"type": "Shield", "objects": ["Wood Shield", "iron Shied"], "picture": "shield.png"},
		]

		self.layout = QBoxLayout(QBoxLayout.LeftToRight, self)
		self.setLayout(self.layout)

		# QTreeView 생성 및 설정
		view = QTreeView(self)
		view.setEditTriggers(QAbstractItemView.DoubleClicked)
		self.model = Model(data)
		view.setModel(self.model)
		self.layout.addWidget(view)

		# 그림을 띄울 QLabel 생성
		self.lb = QLabel()
		self.lb.setFixedSize(50, 50)
		self.layout.addWidget(self.lb)

		# 뷰 클릭시 발생하는 시그널
		# 뷰를 클릭하면 QModelIndex를 넘겨준다.
		view.clicked.connect(self.slot_show_picture)

	@pyqtSlot(QModelIndex)
	def slot_show_picture(self, QModelIndex):
		data = self.model.itemData(QModelIndex)
		if Qt.DecorationRole not in data:
			# DecoreationRole 외는 필요없을 뿐더러 에러가 날 수 있으니 반환처리
			return
		self.lb.setPixmap(QPixmap(data[Qt.DecorationRole]))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
