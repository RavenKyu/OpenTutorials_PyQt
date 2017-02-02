#!/usr/bin/env python
# coding: utf-8

# 예제 내용
# * 겹쳐진 위젯의 순서를 조정한다.

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class StackWidget(QLabel):
	def __init__(self, color, parent=None):
		super(StackWidget, self).__init__(parent)
		self.setStyleSheet("background-color: %s" % color)  # 라벨위젯과의 구분을 위한 색

	def mousePressEvent(self, event):
		"""
		mouse가 위젯 위에서 클릭됐을때만 반응
		"""
		if not self.underMouse():
			return
		self.raise_()


class Form(QWidget):
	def __init__(self):
		QWidget.__init__(self, flags=Qt.Widget)
		self.setWindowTitle("Widget raise and lower")

		self.lb1 = StackWidget("red", parent=self)
		self.lb1.setGeometry(10, 10, 100, 100)

		self.lb2 = StackWidget("pink", parent=self)
		self.lb2.setGeometry(40, 40, 100, 100)

		self.lb3 = StackWidget("yellow", parent=self)
		self.lb3.setGeometry(70, 70, 100, 100)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = Form()
	form.show()
	exit(app.exec_())
