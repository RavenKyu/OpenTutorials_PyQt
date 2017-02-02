#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 위젯의 순서를 찾는 예제

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtCore import qDebug

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)

		self.w1 = QWidget(self, Qt.Widget)
		self.w1.setObjectName("Object_1")

		self.w2 = QWidget(self, Qt.Widget)
		self.w3 = QWidget(self, Qt.Widget)
		self.w4 = QPushButton(self)

		self.w5 = QPushButton(self)
		self.w5.setObjectName("Object_1")

		self.w6 = QLabel()
		self.w6.setObjectName("Object_1")

		self.init_widget()

	def init_widget(self):
		self.setWindowTitle("Find Child Widget")
		templet = "{0:>50} : {1}"
		# 타입 매치
		w_list = self.findChildren(QWidget)
		qDebug(templet.format("type match", w_list))

		# 타입과 오브젝트 이름을 매치
		w_list = self.findChildren(QPushButton, "Object_1")
		qDebug(templet.format("type and object name match", w_list))

		w_list = self.findChildren((QPushButton, QLabel), "Object_1")
		qDebug(templet.format("tuple in types and object name match",  w_list))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	exit(app.exec_())
