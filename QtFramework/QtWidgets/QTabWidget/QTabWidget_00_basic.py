#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * QTabWidget 기본 사용

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QTabWidget
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
		self.setWindowTitle("Tab Widget")
		form_lbx = QBoxLayout(QBoxLayout.TopToBottom, parent=self)
		self.setLayout(form_lbx)

		tbw = QTabWidget()
		form_lbx.addWidget(tbw)

		# 탭 추가
		tbw.addTab(QTextEdit(), "Tab #1")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())