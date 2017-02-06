#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * PushBottun에 단축키 부여

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		# 배치될 위젯 변수 선언
		self.pb_1 = QPushButton()
		self.pb_2 = QPushButton()
		# 레이아웃 선언 및 Form Widget에 설정
		self.layout_1 = QBoxLayout(QBoxLayout.TopToBottom, self)
		self.setLayout(self.layout_1)
		self.init_widget()

	def init_widget(self):
		self.setWindowTitle("PushButton Shortcut")

		# 라벨1의 설정 및 레이아웃 추가
		self.pb_1.setText("Alt + F7")
		self.pb_1.setShortcut("Alt+F7")
		self.layout_1.addWidget(self.pb_1)

		# 라벨2의 설정 및 레이아웃 추가
		self.pb_2.setText("Alt + F8")
		self.pb_2.setShortcut("Alt+F8")
		self.layout_1.addWidget(self.pb_2)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())