#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * RadioButoon 배치

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.setWindowTitle("RadioButton")

		# 배치될 위젯 변수 선언
		rb_1 = QRadioButton("RadioButton 1")
		rb_2 = QRadioButton("RadioButton 2")
		rb_3 = QRadioButton("RadioButton 3")
		rb_4 = QRadioButton("RadioButton 4")
		rb_5 = QRadioButton("RadioButton 5")

		# 레이아웃 선언 및 Form Widget에 설정
		base_layout = QBoxLayout(QBoxLayout.TopToBottom, self)
		base_layout.addWidget(rb_1)
		base_layout.addWidget(rb_2)
		base_layout.addWidget(rb_3)
		base_layout.addWidget(rb_4)
		base_layout.addWidget(rb_5)

		self.setLayout(base_layout)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())