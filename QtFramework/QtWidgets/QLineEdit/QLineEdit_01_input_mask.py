#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QLineEdit 기본 사용

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot


__author__ = "Deokyu Lim <hong18s@gmail.com>"

FORMAT = [
	{"name": "IP ADDRESS", "format": "000.000.000.000;0"},
	{"name": "MAC ADDRESS", "format": "HH:HH:HH:HH:HH:HH;#"},
	{"name": "ISO DATE", "format": "0000-00-00;0"},
	{"name": "LICENSE NUMBER", "format": ">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#"},
]


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.cb = QComboBox()
		self.lb = QLabel()
		self.le = QLineEdit()

		self.init_widget()

	def init_widget(self):
		"""
		현재 위젯의 모양등을 초기화
		"""
		self.setWindowTitle("QLineEdit Widget")
		form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
		self.setLayout(form_lbx)

		# 콤보박스에 아이템 이름과 userRole에 format 정보를 추가
		for item in FORMAT:
			self.cb.addItem(item["name"], item["format"])

		# 시그널 슬롯 처리
		self.cb.currentIndexChanged.connect(self.slot_change_format)
		self.le.textChanged.connect(self.lb.setText)

		form_lbx.addWidget(self.cb)
		form_lbx.addWidget(self.lb)
		form_lbx.addWidget(self.le)

		self.slot_change_format(0)

	@pyqtSlot(int)
	def slot_change_format(self, idx):
		# 콤보박스가 바뀔 때마다
		# 라인에디터 내용, 커서, 마스크 초기화
		# 라벨 내용 초기화
		# 포커스를 라인에디터가 가져감
		self.le.clear()
		self.le.setCursorPosition(0)
		self.le.setInputMask(self.cb.itemData(idx, Qt.UserRole))
		self.lb.clear()
		self.le.setFocus()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())