#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QComboBox 기본 사용

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.init_widget()

	def init_widget(self):
		"""
		현재 위젯의 모양등을 초기화
		"""
		self.setWindowTitle("QComboBox Widget")
		form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
		self.setLayout(form_lbx)

		lb = QLabel()

		qb = QComboBox()
		qb.addItem("Banana")  # 단일 아이템 추가시
		qb.addItems(["Apple", "Tomato", "Carrot"])  # 다수 아이템 추가시
		qb.insertSeparator(2)  # 구분 선
		qb.currentTextChanged.connect(lb.setText)  # 현재 인덱스의 데이터가 바뀔 때

		form_lbx.addWidget(qb)
		form_lbx.addWidget(lb)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())