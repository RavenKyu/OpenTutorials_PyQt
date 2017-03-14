#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QTabWidget 탭에 다양한 위젯 추가

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class TabWidgetA(QWidget):
	def __init__(self, parent=None):
		super(TabWidgetA, self).__init__(parent=parent)
		self.init_widget()

	def init_widget(self):
		"""
		현재 위젯의 모양등을 초기화
		"""
		self.setWindowTitle("Hello World")
		form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
		self.setLayout(form_lbx)

		gb_1 = QGroupBox(self)
		gb_1.setTitle("GroupBox")
		form_lbx.addWidget(gb_1)
		lbx = QBoxLayout(QBoxLayout.LeftToRight)
		gb_1.setLayout(lbx)
		lbx.addWidget(QCheckBox("check box #1"))
		lbx.addWidget(QCheckBox("check box #2"))
		lbx.addWidget(QCheckBox("check box #3"))

		gb_2 = QGroupBox(self)
		gb_2.setTitle("GroupBox")
		gb_2.setCheckable(True)
		gb_2.setChecked(False)
		form_lbx.addWidget(gb_2)
		lbx = QBoxLayout(QBoxLayout.LeftToRight)
		gb_2.setLayout(lbx)
		lbx.addWidget(QRadioButton("radio button #1"))
		lbx.addWidget(QRadioButton("radio button #2"))
		lbx.addWidget(QRadioButton("radio button #3"))


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.tbw = QTabWidget()
		self.init_widget()

	def init_widget(self):
		"""
		현재 위젯의 모양등을 초기화
		"""
		self.setWindowTitle("Tab Widget")
		form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
		self.setLayout(form_lbx)
		form_lbx.addWidget(self.tbw)

		self.tbw.addTab(TabWidgetA(), TabWidgetA.__name__)
		self.tbw.addTab(QTextEdit(), QTextEdit.__name__)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())