#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 위젯의 투명도를 설정한다.

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsOpacityEffect

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)

		# 투명도를 적용할 위젯
		self.w1 = QWidget(parent=self, flags=Qt.Widget)
		self.w3 = QWidget(parent=self, flags=Qt.Widget)
		self.w2 = QWidget(parent=self, flags=Qt.Widget)

		self.init_widget()

	def init_widget(self):
		self.setWindowTitle("Hello World")

		# 맨 아래 놓이게 될 위젯
		# 투명도를 설정하지 않음
		self.w1.setGeometry(10, 10, 100, 100)
		self.w1.setStyleSheet("background-color: yellow")

		# 중간에 놓이게 될 위젯
		# 투명도를 설정하지 않음
		self.w3.setGeometry(40, 40, 100, 100)
		self.w3.setStyleSheet("background-color: pink")

		# 가장 위에 놓이게 될 위젯
		self.w2.setGeometry(70, 70, 100, 100)
		opacity_effect = QGraphicsOpacityEffect(self.w2)
		opacity_effect.setOpacity(0.3)
		self.w2.setGraphicsEffect(opacity_effect)
		self.w2.setStyleSheet("background-color: red")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
