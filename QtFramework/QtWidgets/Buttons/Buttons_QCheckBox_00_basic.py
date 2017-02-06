#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * CheckBox 사용 

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.setWindowTitle("CheckBox")

		# 배치될 위젯 변수 선언
		cb_1 = QCheckBox("CheckBox 1")
		cb_2 = QCheckBox("CheckBox 2")
		cb_3 = QCheckBox("CheckBox 3")
		cb_4 = QCheckBox("CheckBox 4")
		cb_5 = QCheckBox("CheckBox 5")

		# 레이아웃 선언 및 Form Widget에 설정
		base_layout = QBoxLayout(QBoxLayout.TopToBottom, self)
		base_layout.addWidget(cb_1)
		base_layout.addWidget(cb_2)
		base_layout.addWidget(cb_3)
		base_layout.addWidget(cb_4)
		base_layout.addWidget(cb_5)

		self.setLayout(base_layout)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())