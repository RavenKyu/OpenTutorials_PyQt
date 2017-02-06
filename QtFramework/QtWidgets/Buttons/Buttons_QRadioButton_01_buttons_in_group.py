#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * RadioButoon 배치

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.setWindowTitle("RadioButton")

		# 배치될 위젯 변수 선언
		grp_1 = QGroupBox("Group 1")
		grp_2 = QGroupBox("Group 2")
		rb_1 = QRadioButton("RadioButton 1")
		rb_2 = QRadioButton("RadioButton 2")
		rb_3 = QRadioButton("RadioButton 3")
		rb_4 = QRadioButton("RadioButton 4")
		rb_5 = QRadioButton("RadioButton 5")

		# 레이아웃 선언 및 Form Widget에 설정
		base_layout = QBoxLayout(QBoxLayout.TopToBottom, self)
		grp_1_layout = QBoxLayout(QBoxLayout.TopToBottom)
		grp_2_layout = QBoxLayout(QBoxLayout.TopToBottom)

		grp_1.setLayout(grp_1_layout)
		grp_2.setLayout(grp_2_layout)

		grp_1_layout.addWidget(rb_1)
		grp_1_layout.addWidget(rb_2)
		grp_1_layout.addWidget(rb_3)
		grp_2_layout.addWidget(rb_4)
		grp_2_layout.addWidget(rb_5)

		base_layout.addWidget(grp_1)
		base_layout.addWidget(grp_2)

		self.setLayout(base_layout)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())