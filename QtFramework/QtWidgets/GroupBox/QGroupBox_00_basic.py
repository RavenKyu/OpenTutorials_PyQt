#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QGroupBox에 위젯을 넣어 정렬

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.init_widget()

	def init_widget(self):
		"""
		현재 위젯의 모양등을 초기화
		"""
		self.setWindowTitle("Hello World")
		form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
		self.setLayout(form_lbx)

		# 1번 그룹박스 생성
		gb_1 = QGroupBox(self)
		gb_1.setTitle("GroupBox")
		form_lbx.addWidget(gb_1)
		lbx = QBoxLayout(QBoxLayout.LeftToRight, parent=self)
		gb_1.setLayout(lbx)
		lbx.addWidget(QCheckBox("check box #1"))
		lbx.addWidget(QCheckBox("check box #2"))
		lbx.addWidget(QCheckBox("check box #3"))

		# 2번 그룹박스, 사용여부 체크가 가능, 기본 값으로 사용안함
		gb_2 = QGroupBox(self)
		gb_2.setTitle("GroupBox")
		gb_2.setCheckable(True)
		gb_2.setChecked(False)
		form_lbx.addWidget(gb_2)
		lbx = QBoxLayout(QBoxLayout.LeftToRight, parent=self)
		gb_2.setLayout(lbx)
		lbx.addWidget(QRadioButton("radio button #1"))
		lbx.addWidget(QRadioButton("radio button #2"))
		lbx.addWidget(QRadioButton("radio button #3"))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())