#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QListView 기본 사용법
# * QAbstractListModel 을 이용한 사용자 모델 생성
# * 수정이 가능한 모델

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QListView
from PyQt5.QtCore import QAbstractListModel
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import QVariant
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class UserModel(QAbstractListModel):
	"""
	ListModel은 두 가지의 필수 메소드를 작성해야 한다.
	int rowCount(self, parent=None, *args, **kwargs)
	QVariant data(self, QModelIndex, role=None)
	"""
	def __init__(self, data=None, parent=None):
		QAbstractListModel.__init__(self, parent)
		self._data = data

	def rowCount(self, parent=None, *args, **kwargs):
		"""
		데이터의 개 수를 반환
		"""
		return len(self._data)

	def data(self, QModelIndex, role=None):
		"""
		어떠한 이벤트가 일어났을 때 View가 Model.data를 호출
		View의 요구를 role을 참고하여 해당하는 값을 반환
		해당하는 role에 대한 대응이 없을 경우 QVariant를 반환
		"""
		item = self._data[QModelIndex.row()]

		if role == Qt.DisplayRole:  # 값 출력시
			return "%s" % item['name']
		elif role == Qt.EditRole:  # 값 수정시
			return "%s" % item['name']
		return QVariant()

	def flags(self, QModelIndex):
		"""
		모델 아이템별에 대한 정책
		"""
		return Qt.ItemIsEditable | Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsTristate

	def setData(self, QModelIndex, value, role=None):
		"""
		값 수정시 호출
		"""
		self._data[QModelIndex.row()]['name'] = value
		return True
	

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
		view.setEditTriggers(QAbstractItemView.DoubleClicked)

		model = UserModel(fruits)
		view.setModel(model)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
